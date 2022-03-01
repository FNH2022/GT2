
import PIL

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
percent = 40  # Percent for gauge
output_file_name = '/content/new_gauge.png'

# X and Y coordinates of the center bottom of the needle starting from the top left corner
#   of the image
x = 825
y = 825
loc = (x, y)

percent = percent / 100
rotation = 180 * percent  # 180 degrees because the gauge is half a circle
rotation = 90 - rotation  # Factor in the needle graphic pointing to 50 (90 degrees)

dial = Image.open('/content/needle.png')
dial = dial.rotate(rotation, resample=PIL.Image.BICUBIC, center=loc)  # Rotate needle

gauge = Image.open('/content/gauge.png')
gauge.paste(dial, mask=dial)  # Paste needle onto gauge
gauge.save(output_file_name)
new = Image.open("/content/new_gauge.png")
new.show()
