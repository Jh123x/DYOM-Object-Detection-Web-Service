"""
The file containing the code for detecting the objects in the image.

Adapted from YOLO v5: https://github.com/ultralytics/yolov5

"""
# Import yolo5s model
import torch  
from PIL import Image

# Create the Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')


def draw_bounding_boxes(image_binary: bytes) -> Image:
    """Generate the image with the bounding boxes"""
    image = Image.open(image_binary)

    # Run the detector to generate the boxes
    img = model(image)

    # Load the bounding boxes into the img
    img.render()
    # Transform image
    result = Image.fromarray(img.imgs[0])

    return result
