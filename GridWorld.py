from fractions import *


def get_blocked_probability(p):
    


def generate_grid(dim):
    grid = []
    x = 0
    y = 0
    while(x<dim):
        temp = []
        y = 0
        while(y<dim):
            temp.append(0)
            y += 1
        grid.append(temp)
        x += 1
    return grid
