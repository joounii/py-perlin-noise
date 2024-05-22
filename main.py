import math
import random
from array import array
from colored_print import log
from render_gui import render

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(t, a, b):
    return a + t * (b - a)

def grad(hash, x, y):
    h = hash & 7
    u = x if h < 4 else y
    v = y if h < 4 else x
    return (u if h & 1 == 0 else -u) + (v if h & 2 == 0 else -v)

def perlin(x, y, perm):
    X = int(x) & 255
    Y = int(y) & 255
    
    x -= int(x)
    y -= int(y)
    
    u = fade(x)
    v = fade(y)
    
    aa = perm[perm[X] + Y]
    ab = perm[perm[X] + Y + 1]
    ba = perm[perm[X + 1] + Y]
    bb = perm[perm[X + 1] + Y + 1]
    
    return lerp(v, lerp(u, grad(aa, x, y), grad(ba, x - 1, y)),
                   lerp(u, grad(ab, x, y - 1), grad(bb, x - 1, y - 1)))

def generate_perlin_noise(width, height, scale=100):
    random.seed(0)
    perm = list(range(256))
    random.shuffle(perm)
    perm += perm  # duplicate the permutation list
    
    noise = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            nx = x / scale
            ny = y / scale
            noise[y][x] = perlin(nx, ny, perm)
    
    return noise

def print_noise(noise):
    for row in noise:
        print("".join(f"{val:.2f} " for val in row))
        
def create_array_for_rendering():
    flattened_list_noise_list = [element for row in noise for element in row]
    min_value = min(flattened_list_noise_list)
    # log.success(min_value)
    positiv_noise_list = [[(element + (min_value * -1)) * 100 for element in row] for row in noise]
    flattened_list_positiv_list = [element for row in positiv_noise_list for element in row]
    max_value = max(flattened_list_positiv_list)
    min_value = min(flattened_list_positiv_list)
    # log.success(max_value)
    # log.success(min_value)
    
    # print("------------------")
    # print_noise(positiv_noise_list)
    render(positiv_noise_list, max_value)


if __name__ == "__main__":
    log.warn("started calculating array...")
    width = 1000 #249
    height = 1000 #123
    scale = 30
    noise = generate_perlin_noise(width, height, scale)
    # noise_array = array("i", noise)
    # print_noise(noise)
    log.success("successfuly calculated array")
    create_array_for_rendering()