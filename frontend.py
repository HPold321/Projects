import streamlit as st
from PIL import Image
from object_detector import detect_objects, load_model

st.title("Object Detection App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")

    if st.button('Detect'):
        model_path = "/home/ananya/Documents/yolov8_pytorch/runs/detect/train4/weights/best.pt"
        config_path = "/home/ananya/Documents/yolov8_pytorch/dataset/data.yaml"
        model, names = load_model(model_path, config_path)
        # Perform detection
        output = detect_objects(uploaded_file, model, names)
        # Process output and display annotated image
        # You can modify this part based on the output format and how you want to visualize the results
        annotated_image = process_output(output, image)
        st.image(annotated_image, caption='Annotated Image.', use_column_width=True)

