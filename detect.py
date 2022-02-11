
import argparse
import cv2
import os

from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference
import PIL

from PIL import Image

percent = 20  # Percent for gauge
output_file_name = 'new_gauge.png'

# X and Y coordinates of the center bottom of the needle starting from the top left corner
#   of the image
x = 825
y = 825
loc = (x, y)

percent = percent / 100
rotation = 180 * percent  # 180 degrees because the gauge is half a circle
rotation = 90 - rotation  # Factor in the needle graphic pointing to 50 (90 degrees)

dial = Image.open('needle.png')
dial = dial.rotate(rotation, resample=PIL.Image.BICUBIC, center=loc)  # Rotate needle

gauge = Image.open('gauge.png')
gauge.paste(dial, mask=dial)  # Paste needle onto gauge
gauge.save(output_file_name)

def append_objs_to_img(cv2_im, inference_size, objs, labels):
    height, width, channels = cv2_im.shape
    scale_x, scale_y = width / inference_size[0], height / inference_size[1]
    for obj in objs:
        bbox = obj.bbox.scale(scale_x, scale_y)
        x0, y0 = int(bbox.xmin), int(bbox.ymin)
        x1, y1 = int(bbox.xmax), int(bbox.ymax)

        percent = int(100 * obj.score)
        label = '{}% {}'.format(percent, labels.get(obj.id, obj.id))

        cv2_im = cv2.rectangle(cv2_im, (x0, y0), (x1, y1), (0, 255, 0), 2)
        cv2_im = cv2.putText(cv2_im, label, (x0, y0+30),
                             cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2)
    return cv2_im

