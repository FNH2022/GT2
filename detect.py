
import argparse
import random

import cv2
import os
import PIL

from PIL import Image

from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference

        x = 825
        y = 825
        loc = (x, y)
        percent = random.randint(1, 90)  # Percent for gauge
        output_file_name = 'new_gauge.png'
        percent = percent / 100
        rotation = 180 * percent  # 180 degrees because the gauge is half a circle
        rotation = 90 - rotation  # Factor in the needle graphic pointing to 50 (90 degrees)

        dial = Image.open('needle.png')
        dial = dial.rotate(rotation, resample=PIL.Image.BICUBIC, center=loc)  # Rotate needle

        gauge = Image.open('gauge.png')
        gauge.paste(dial, mask=dial)  # Paste needle onto gauge
        gauge.save(output_file_name)    
        gauge.imshow(output_file_name)
