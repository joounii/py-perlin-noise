import tkinter as tk
from tkinter import ttk
from numpy import *

def get_color(value, max_value):
    color = hex(int(255 / max_value * value)).replace('0x', '') * 3
    print(color)
    print(type(color))
    return color

def render(data_array, max_value):
    root = tk.Tk()
    # root.geometry("240x100")
    root.title('Perlin Noise')
    # root.resizable(0, 0)
    canvas = tk.Canvas(root)
    height = 0
    width = 0
    pixel_size = 3
    
    for i in data_array:
        for x in i:
            canvas.create_rectangle(10 + pixel_size * width, 10 + pixel_size * height, 30 + pixel_size * width, 30 + pixel_size * height, fill = "#" + get_color(x, max_value), width = 0)
            width += 1
        height += 1
        width = 0

    # canvas.create_rectangle(10, 10, 30, 30, outline = "black", fill = "blue", width = 2)
    # canvas.create_rectangle(10, 30, 30, 50, outline = "black", fill = "blue", width = 2)

    canvas.pack(fill = "both", expand = True)

    root.mainloop()

# perlin_array = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]   
# render(perlin_array)