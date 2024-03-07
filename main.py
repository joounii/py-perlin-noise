from render_gui import render
import random

height = 100
width = 100

color_scale = 100

start_points = 5

perlin_array = []

i = 0
x = 0
while i < height:
    width_array = []
    while x < width:
        width_array.extend([random.randint(0,color_scale)])
        x += 1
    perlin_array.extend([width_array])

    i += 1
    x = 0

render(perlin_array, color_scale)
print(perlin_array)