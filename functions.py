from PIL import Image, ImageDraw, ImageFilter  # imports the library
import math

#original = Image.open("./images/pi.jpg") # load an image from the hard drive
#blurred = original.filter(ImageFilter.BLUR) # blur the image

def simple_line(intx1, inty1, intx2, inty2, pencil, color):
    dy = inty2 - inty1
    dx = intx2 - intx1
    m = dy / dx
    y = inty1
    x = intx1
    for x in range(x, intx2+1):
        floor_y = math.floor((int)(y + 0.5))
        pencil.point([x, floor_y], color)
        y += m

def midpoint_line(intx1, inty1, intx2, inty2, pencil, color):
    dx = intx2 - intx1
    dy = inty2 - inty1
    d = dy * 2 - dx
    incrE = dy * 2
    incrNE = (dy - dx) *2
    x = intx1
    y = inty1
    pencil.point([intx1, inty1], color)
    while x < intx2:
        if d <= 0:
            d += incrE
            x += 1
        else:
            d += incrNE
            x += 1
            y += 1
        pencil.point([x, y], color)

def circle_points(x, y, centre_x, centre_y, pencil, color):
    pencil.point([x + centre_x, y + centre_y], color)
    pencil.point([y + centre_x, x + centre_y], color)
    pencil.point([y + centre_x, -x + centre_y], color)
    pencil.point([x + centre_x, -y + centre_y], color)
    pencil.point([-x + centre_x, -y + centre_y], color)
    pencil.point([-y + centre_x, -x + centre_y], color)
    pencil.point([-y + centre_x, x + centre_y], color)
    pencil.point([-x + centre_x, y + centre_y], color)

def midpoint_circle(radius, centre_x, centre_y, pencil, color):
    x = 0
    y = radius
    d = 5.0/4 - radius
    circle_points(x, y, centre_x, centre_y, pencil, color)
    while y > x:
        if d < 0:
            d += x * 2.0 + 3
            x += 1
        else:
            d += (x - y) * 2.0 + 5
            x += 1
            y -= 1
        circle_points(x, y, centre_x, centre_y, pencil, color)

canvas = Image.new('RGBA', (600, 300), color='white')
pencil = ImageDraw.Draw(canvas)

simple_line(34, 89, 278, 130, pencil, 'green')
midpoint_line(34, 95, 278, 135, pencil, 'red')

midpoint_circle(100, 250, 150, pencil, 'blue')

canvas.show()