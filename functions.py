from PIL import Image, ImageDraw, ImageFilter  # imports the library
import math

#original = Image.open("./images/pi.jpg") # load an image from the hard drive
#blurred = original.filter(ImageFilter.BLUR) # blur the image

def simple_line(intx1, inty1, intx2, inty2, pencil, color, canvas):
    dy = inty2 - inty1
    dx = intx2 - intx1
    m = dy / dx
    y = inty1
    x = intx1
    for x in range(x, intx2+1):
        floor_y = math.floor((int)(y + 0.5))
        pencil.point([x, floor_y], color)
        y += m

canvas = Image.new('RGBA', (600, 300), color='white')
pencil = ImageDraw.Draw(canvas)

simple_line(34, 89, 278, 130, pencil, 'green', canvas)

canvas.show()