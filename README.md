# Projects
This is how this module of streamlit-frontend works. But first let's get to know about the project. 


# Streamlit Object Detection App

This project is a Streamlit web application for object detection in images and videos using the YOLO (You Only Look Once) deep learning algorithm. Specifically, it uses the version 8 of YOLO. 

## Features

- Allows users to upload images or videos for object detection.
- Supports detection in both images and videos.
- Real-time annotation of detected objects.
- Provides options to either upload files from the local machine or enter URLs.
- Supports stopping the detection process (for videos) via a keyboard shortcut (Ctrl+Q).
- Uses YOLOv8 in integration with SAHI for object detection in images and videos. 

## Installation

1. Clone the repository:


2. Install the required dependencies:

    ```bash
    pip3 install sahi
    pip3 install ultralytics
    pip3 install yolov8
    pip3 install streamlit
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run run.py
    ```

2. Open the provided URL in your web browser.

3. Select the input method: either upload files from your computer or enter URLs.

4. Upload an image or video file or enter a URL and click "Submit".

5. For video detection, you can press Ctrl+Q to stop the detection process at any time.

6. View the annotated images or videos with detected objects.
