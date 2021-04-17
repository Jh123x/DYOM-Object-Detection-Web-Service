# DYOM Object Detection Web Service
An object detection service for Machine Learning in Practice (DYOM1401TT)

# Quick Start guide

1. Run the below in your shell to install the requirements
    ```python
    # For windows
    python -m pip install -r requirements.txt

    # For Unix
    pip3 install -r requirements.txt
    ```
1. Run `python3 __main__.py` (Unix) or `python __main__.py` (Windows) to start the server
1. The server will run at `localhost` port 80 by default
1. Go to `http://localhost` to enjoy the webservice


# What does it do
- It is a webservice that allows the user to upload an Image and and draw bounding boxes for the object it detects within the image
- It makes use of [yolo5](https://github.com/ultralytics/yolov5) and its pretrained weights for this.

# Tech Stack
1. [Pytorch](https://pytorch.org/)
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)