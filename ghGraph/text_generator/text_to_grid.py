from PIL import ImageFont, ImageDraw,Image
import numpy as np

#creating a new image in black background and filling it with white text

tempImage = Image.new(mode = 'RGB',size = (100,100),color = '#000000')
draw = ImageDraw.Draw(tempImage)
font = ImageFont.truetype("fonts/PixeloidSans.ttf",15)

#looping to find the suitable font size
text = "HELLO"
imgWidth, imgHeight = 520,70
fontPath = "fonts/PixeloidSans.ttf"
fontSize = 8

while True:
    try:
        font = ImageFont.truetype(fontPath, fontSize)
        ascent, descent = font.getmetrics()
        currWidth = int(font.getlength(text))
        currHeight = ascent + descent
        if(currWidth >= imgWidth or currHeight >= imgHeight):
            fontSize -= 1
            break
        fontSize += 1
    except OSError:
        fontSize -= 1
        break
bgImage = Image.new(mode = 'L', size= (currWidth, currHeight), color = "#000000")
draw = ImageDraw.Draw(bgImage)
draw.text((0,0),"HELLO",font = font,fill='white')
bgImage.show()
