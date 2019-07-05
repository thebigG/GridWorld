from random import random
import math
BLOCKED = 1
UNBLOCKED = 0

def euclidean_distance(x1,y1,x2,y2):
    return math.sqrt(pow((x1 - x2),2) + pow((y1 - y2), 2))

def manhattan_distance(x1,y1,x2,y2):
    return abs( x1 - x2 ) + abs(y1 - y2)


def chebyshev_distance(x1,y1,x2,y2):
    """
    This function is also known as chess distance. That means how many moves it'll
    take the king to move from (x1,y1) to (x2,y2), if the grid were a chess board.
    """
    return max(abs((x1) - (x2) ), abs(y1 - y2))

def move_agent_north(grid, agent_position):
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    grid[x_agent_position][y_agent_position], grid[x_agent_position-1][y_agent_position]  = grid[x_agent_position- 1], grid[y_agent_position], grid[x_agent_position][y_agent_position]
    print_grid(grid)

def move_agent_south(grid, agent_position):
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    grid[x_agent_position][y_agent_position], grid[x_agent_position+1][y_agent_position]  = grid[x_agent_position+ 1][y_agent_position], grid[x_agent_position][y_agent_position]
    print_grid(grid)

def move_agent_east(grid, agent_position):
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    grid[x_agent_position][y_agent_position], grid[x_agent_position][y_agent_position+1]  = grid[x_agent_position][y_agent_position+1], grid[x_agent_position][y_agent_position]
    print_grid(grid)


def move_agent_west(grid, agent_position):
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    grid[x_agent_position][y_agent_position], grid[x_agent_position][y_agent_position-1]  = grid[x_agent_position][y_agent_position-1], grid[x_agent_position][y_agent_position]
    print_grid(grid)

def look_and_tell_south_cell(grid,agent_position):
    """
    Looks and tell if the south cell, relative to agent_position, is blocked or not.
    If it is unblocked, this function returns True. If it is blocked, it returns false.
    """
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    return grid[x_agent_position+1][y_agent_position]==UNBLOCKED

def look_and_tell_north_cell(grid,agent_position):
    """
    Looks and tell if the north cell, relative to agent_position, is blocked or not.
    If it is unblocked, this function returns True. If it is blocked, it returns false.
    """
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    return grid[x_agent_position-1][y_agent_position]==UNBLOCKED

def look_and_tell_east_cell(grid,agent_position):
    """
    Looks and tell if the east cell, relative to agent_position, is blocked or not.
    If it is unblocked, this function returns True. If it is blocked, it returns false.
    """
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    return grid[x_agent_position][y_agent_position+1]==UNBLOCKED

def look_and_tell_west_cell(grid,agent_position):
    """
    Looks and tell if the west cell, relative to agent_position, is blocked or not.
    If it is unblocked, this function returns True. If it is blocked, it returns false.
    """
    x_agent_position = agent_position[0]
    y_agent_position = agent_position[1]
    return grid[x_agent_position][y_agent_position-1]==UNBLOCKED

def is_cell_blocked(p):
    random_num = random()
    return random_num<=p

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
    grid[0][0] = 'S'
    grid[dim-1][dim-1] = 'G'
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
