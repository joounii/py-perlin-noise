from render_gui import render

height = 100
width = 100

start_points = 5

perlin_array = []

i = 0
x = 0
while i < height:
    width_array = []
    while x < width:
        width_array.extend([1])
        x += 1
    perlin_array.extend([width_array])

    i += 1
    x = 0

render(perlin_array)
print(perlin_array)