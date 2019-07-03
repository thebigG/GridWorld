from random import random

BLOCKED = 1
UNBLOCKED = 0

def is_cell_blocked(p):
    random_num = random()
    if random_num<=p:
        return True
    else:
        return False

def generate_grid(dim, p):
    grid = []
    x = 0
    y = 0
    while(x<dim):
        temp = []
        y = 0
        while(y<dim):
            # The ugly-looking statements are just making sure we don't block the Start or Goal cells.
            if( ((x!=0 or y!=0) and (x!=(dim-1) or (y!=dim-1)))  and is_cell_blocked(p) ):
                temp.append(BLOCKED)
            else:
                temp.append(UNBLOCKED)
            y += 1
        grid.append(temp)
        x += 1
    return grid


def print_grid(grid):
    """
    ALWAYS call print_grid to print ANY grid. DO NOT call python's built-in print().
    """
    formatted_grid = ""
    for row in grid:
        formatted_grid += str(row)
        formatted_grid += "\n"
    print(formatted_grid)
