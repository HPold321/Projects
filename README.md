# yolov8-objDetection
This is how this module of streamlit-frontend works. But first let's get to know about the project. 


# Streamlit Object Detection App

This project is a Streamlit web application for object detection in images and videos using the YOLO (You Only Look Once) deep learning algorithm. Specifically, it uses the version 8 of YOLO. 

## Features

- Allows users to upload images or videos for object detection.
- Supports detection in both images and videos.
- Real-time bounding boxes createdc on actual images of deected objects.
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

## Contributing
Ultralytics...
{
cff-version: 1.2.0
title: Ultralytics YOLO
message: >-
  If you use this software, please cite it using the
  metadata from this file.
type: software
authors:
  - given-names: Glenn
    family-names: Jocher
    affiliation: Ultralytics
    orcid: 'https://orcid.org/0000-0001-5950-6979'
  - given-names: Ayush
    family-names: Chaurasia
    affiliation: Ultralytics
    orcid: 'https://orcid.org/0000-0002-7603-6750'
  - family-names: Qiu
    given-names: Jing
    affiliation: Ultralytics
    orcid: 'https://orcid.org/0000-0003-3783-7069'
repository-code: 'https://github.com/ultralytics/ultralytics'
url: 'https://ultralytics.com'
license: AGPL-3.0
version: 8.0.0
date-released: '2023-01-10' }


obss/ sahi...
{
cff-version: 1.2.0
message: "If you use this package, please consider citing it."
authors:
- family-names: "Akyon"
  given-names: "Fatih Cagatay"
- family-names: "Cengiz"
  given-names: "Cemil"
- family-names: "Altinuc"
  given-names: "Sinan Onur"
- family-names: "Cavusoglu"
  given-names: "Devrim"
- family-names: "Sahin"
  given-names: "Kadir"
- family-names: "Eryuksel"
  given-names: "Ogulcan"
title: "SAHI: A lightweight vision library for performing large scale object detection and instance segmentation"
preferred-citation:
  type: article
  title: "Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection"
  doi: 10.1109/ICIP46576.2022.9897990
  url: https://ieeexplore.ieee.org/document/9897990
  journal: 2022 IEEE International Conference on Image Processing (ICIP)
  authors:
  - family-names: "Akyon"
    given-names: "Fatih Cagatay"
  - family-names: "Altinuc"
    given-names: "Sinan Onur"
  - family-names: "Temizel"
    given-names: "Alptekin"
  year: 2022
  start: 966
  end: 970
}
