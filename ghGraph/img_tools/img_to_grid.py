from PIL import Image
import numpy as np

img = Image.open("hello.png")
imgArray = np.asarray(img)
imgArrayDown = imgArray.reshape(7, 10, 52, 10).mean(axis=(1, 3))
levels = " ░▒▓█"  # 5 levels of shade

for row in imgArrayDown:
    line = ""
    for val in row:
        idx = int(val / 255 * (len(levels) - 1))  # normalize to 0-4
        line += levels[idx]
    print(line)
