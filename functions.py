from PIL import Image, ImageDraw, ImageColor, ImageFilter  # imports the library
from win32api import GetSystemMetrics
import math, randomcolor, random

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

def fill_midpoint_circle(radius, centre_x, centre_y, pencil, color):
    while radius > 0:
        midpoint_circle(radius, centre_x, centre_y, pencil, color)
        radius -= 1

def random_circle_dimensions(width, height):
    circle_dim = []
    circle_dim.append(random.randint(20,250))
    circle_dim.append(random.randint(0 - math.ceil(circle_dim[0]/2), width + math.floor(circle_dim[0]/2)))
    circle_dim.append(random.randint(0 - math.ceil(circle_dim[0]/2), height + math.floor(circle_dim[0]/2)))
    return circle_dim

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

color_generator = randomcolor.RandomColor()
bg_color = color_generator.generate()
color_list = color_generator.generate(count=3)

canvas = Image.new('RGBA', (width, height), bg_color[0])
pencil = ImageDraw.Draw(canvas)

test_dimensions = random_circle_dimensions(width, height)
print(test_dimensions)
fill_midpoint_circle(test_dimensions[0], test_dimensions[1], test_dimensions[2], pencil, random.choice(color_list))

canvas.show()