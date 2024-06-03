import streamlit as st
import os
import requests
from detect import setup_model, detect_objects_in_image, detect_objects_in_video

IMAGE_DIR = "/home/ananya/Documents/streamlit-frontend/data/Images"
VIDEO_DIR = "/home/ananya/Documents/streamlit-frontend/data/Videos"

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

def save_uploaded_file(uploaded_file, save_dir, prefix):
    file_extension = os.path.splitext(uploaded_file.name)[1]
    if file_extension.lower() not in ['.avi', '.mp4', '.mov', '.png', '.jpg', '.jpeg']:
        st.error("Unsupported file format.")
        return None
    
    files = os.listdir(save_dir)
    next_index = len(files) + 1
    save_path = os.path.join(save_dir, f"{prefix}_{next_index:03d}{file_extension}")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def save_url_file(url, save_dir, prefix):
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Failed to download the file.")
        return None

    file_extension = os.path.splitext(url)[1]
    if file_extension.lower() not in ['.avi', '.mp4', '.mov', '.png', '.jpg', '.jpeg']:
        st.error("Unsupported file format.")
        return None

    files = os.listdir(save_dir)
    next_index = len(files) + 1
    save_path = os.path.join(save_dir, f"{prefix}_{next_index:03d}{file_extension}")
    with open(save_path, "wb") as f:
        f.write(response.content)
    return save_path

def main():
    st.header('Module Input')

    option = st.radio("Select Input Method:", ('Upload from Computer', 'URL'))

    if option == 'Upload from Computer':
        with st.expander('Upload File'):
            file = st.file_uploader("Choose a file", type=['avi', 'mp4', 'mov', 'png', 'jpg', 'jpeg'])
            if file is not None:
                if st.button('Submit'):
                    if file.type.startswith('image'):
                        file_path = save_uploaded_file(file, IMAGE_DIR, 'IMG')
                        if file_path:
                            detection_model = setup_model()
                            annotated_path = detect_objects_in_image(file_path, detection_model)
                            st.image(annotated_path)
                            st.write(f"Annotated image saved at: {annotated_path}")
                    elif file.type.startswith('video'):
                        file_path = save_uploaded_file(file, VIDEO_DIR, 'Video')
                        if file_path:
                            annotated_path = detect_objects_in_video(file_path)
                            st.text(f"Annotated video saved at: {annotated_path}")
                            # st.video(annotated_path)

    elif option == 'URL':
        with st.expander('Enter URL'):
            url = st.text_input('Enter URL:')
            if st.button('Submit'):
                if url.endswith(('.avi', '.mp4', '.mov', '.png', '.jpg', '.jpeg')):
                    file_extension = os.path.splitext(url)[1]
                    if file_extension.lower() in ['.png', '.jpg', '.jpeg']:
                        file_path = save_url_file(url, IMAGE_DIR, 'IMG')
                        if file_path:
                            detection_model = setup_model()
                            annotated_path = detect_objects_in_image(file_path, detection_model)
                            st.image(annotated_path)
                            st.write("Image saved in ", annotated_path)
                    elif file_extension.lower() in ['.avi', '.mp4', '.mov']:
                        file_path = save_url_file(url, VIDEO_DIR, 'Video')
                        if file_path:
                            annotated_path = detect_objects_in_video(file_path)
                            st.video(annotated_path)
                            st.write("Video saved in ", annotated_path)
                else:
                    st.error("URL must end with .avi, .mp4, .mov, .png, .jpg, or .jpeg")

def display_output(input_data):
    st.write('Output:', input_data)

if __name__ == "__main__":
    main()
