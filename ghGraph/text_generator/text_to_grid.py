from PIL import ImageFont, ImageDraw,Image

image = Image.new(mode = 'RGB',size = (100,70),color = '#ffffff')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("fonts/PixeloidSans.ttf",15)
draw.text((52,7),"world",font = font,fill = 'black')
image.show()
