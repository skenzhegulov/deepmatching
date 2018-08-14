import deepmatching as dm
import numpy as np
from PIL import Image

im1 = np.array(Image.open('liberty1.png'))
im2 = np.array(Image.open('liberty2.png'))

matches = dm.deepmatching(im1, im2, '-downscale 2 -v')

print(matches)
