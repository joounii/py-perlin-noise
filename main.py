from render_gui import render
import random

height = 100
width = 100

color_scale = 100

start_points = 5

perlin_array = []

last_color = random.randint(0,color_scale)

color_change = 10

first_row = True
first_pixel_in_row = True

i = 0
x = 0

# current logic: 
# step 1: generate a random number between 0 and the color_scale
# step 2: with that random number generate a random number that is +/- 10 from the generated number befor
# step 3: repeat this step until the max witdth is reacht but always use the random number generated befor to calculate the new value with +/- 10
# step 4: after the first row of pixel is generated get the pixel abofe and calculated the averag between the left and the above pixel to get the base pixel
# step 5: use the new base pixel to generate the current pixel with +/- 10 and repeat from step 4 until all pixels are generated

while i < height:
    width_array = []
    while x < width:
        if(first_row):
            if(last_color - color_change >= 0 and last_color + color_change <= color_scale):
                new_color = random.randint(last_color - color_change, last_color + color_change)
            elif(last_color - color_change <= 0):
                new_color = random.randint(last_color, last_color + color_change)
            elif(last_color + color_change >= color_scale):
                new_color = random.randint(last_color - color_change, last_color)
        else:
            if(first_pixel_in_row):
                last_color = perlin_array[i -1][x]
            else:
                last_color = (perlin_array[i -1][x] + last_color) / 2
            if(last_color - color_change >= 0 and last_color + color_change <= color_scale):
                new_color = random.randint(last_color - color_change, last_color + color_change)
            elif(last_color - color_change <= 0):
                new_color = random.randint(last_color, last_color + color_change)
            elif(last_color + color_change >= color_scale):
                new_color = random.randint(last_color - color_change, last_color)
        
        width_array.extend([new_color])
        last_color = new_color
        x += 1
    perlin_array.extend([width_array])
    first_row = False
    i += 1
    x = 0

render(perlin_array, color_scale)
print(perlin_array)