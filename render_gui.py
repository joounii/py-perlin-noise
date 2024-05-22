import tkinter as tk
from tkinter import ttk
from numpy import *
from colored_print import log

def get_color(value, max_value):
    color = hex(int(255 / max_value * value)).replace('0x', '')
     # use the hex color value to creat a hex color code
    if(len(color) != 2):
        color = ("0" + color) * 3
        # log.warn("fixed color code: " + color)
    else:
        color = color * 3
    # print(color)
    return color

def render(data_array, max_value):
    
    log.warn("stared rendering...")
    root = tk.Tk()
    # root.geometry("240x100")
    root.title('Perlin Noise')
    # root.resizable(0, 0)
    canvas = tk.Canvas(root)
    height = 0
    width = 0
    pixel_size = 5
    
    for i in data_array:
        for x in i:
            canvas.create_rectangle(10 + pixel_size * width, 10 + pixel_size * height, 30 + pixel_size * width, 30 + pixel_size * height, fill = "#" + get_color(x, max_value), width = 0)
            width += 1
        height += 1
        width = 0

    # canvas.create_rectangle(10, 10, 30, 30, outline = "black", fill = "blue", width = 2)
    # canvas.create_rectangle(10, 30, 30, 50, outline = "black", fill = "blue", width = 2)

    canvas.pack(fill = "both", expand = True)

    log.success("rendering done!")

    root.mainloop()

# perlin_array = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]   
# render(perlin_array)