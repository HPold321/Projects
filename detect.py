import os
from sahi.utils.yolov8 import download_yolov8s_model
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
import subprocess
from pynput import keyboard
import time

def setup_model():
    # Download and set up the YOLOv8 model
    download_yolov8s_model()
    detection_model = AutoDetectionModel.from_pretrained(
        model_path="yolov8s.pt",  # path to your downloaded YOLOv8 model
        model_type="yolov8",      # model type
        confidence_threshold=0.45  # confidence threshold for detection
    )
    return detection_model

def detect_objects_in_image(image_path, detection_model):
    result = get_sliced_prediction(
        image_path,
        detection_model=detection_model,
        slice_height=256,
        slice_width=256,
        overlap_height_ratio=0.2,
        overlap_width_ratio=0.2
    )

    file_name = os.path.basename(image_path)
    annotated_file_name = f"Annotated{file_name}"
    annotated_path = os.path.join(os.path.dirname(image_path), annotated_file_name)

    result.export_visuals(export_dir=os.path.dirname(image_path))
    os.rename(os.path.join(os.path.dirname(image_path), "prediction_visual.png"), annotated_path)
    
    return annotated_path

def detect_objects_in_video(video_path):
    base_output_dir = "/home/ananya/Documents/streamlit-frontend/runs/detect"  # Base directory where YOLO outputs are saved

    # Start the YOLO process
    process = subprocess.Popen(
        ["yolo", "task=detect", "mode=predict", f"source={video_path}", "model=yolov8n.pt", "show=True"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Define a function to stop the process
    def stop_process():
        process.terminate()

    # Define a callback function for key press events
    def on_press(key):
        try:
            if key.char == 'q' and 'ctrl' in current_keys:
                stop_process()
                return False  # Stop the listener
        except AttributeError:
            if key == keyboard.Key.ctrl_l:
                current_keys.add('ctrl')

    def on_release(key):
        if key == keyboard.Key.ctrl_l:
            current_keys.discard('ctrl')

    # Create a listener for keyboard events
    current_keys = set()
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

    # Wait for the process to finish
    process.wait()

    # Give some time for the output files to be written
    time.sleep(1)

    # Find the latest directory in the base output directory
    output_subdirs = [os.path.join(base_output_dir, d) for d in os.listdir(base_output_dir) if os.path.isdir(os.path.join(base_output_dir, d))]
    latest_output_dir = max(output_subdirs, key=os.path.getmtime)

    # Check the latest output directory for the annotated video
    output_files = os.listdir(latest_output_dir)
    annotated_video = [file for file in output_files if file.endswith(('.avi', '.mp4', '.mov'))]
    if annotated_video:
        return os.path.join(latest_output_dir, annotated_video[0])
    return None
