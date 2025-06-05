from text_to_img import getTextImage
from PIL import Image
import numpy as np
img = getTextImage("hello","fonts/PixeloidSans.ttf")
img.save('hello.png')
npArray = np.asarray(img)
print(npArray.shape)
