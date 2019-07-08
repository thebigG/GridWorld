from random import random
import math
import sys
import time

def euclidean_distance(x1,y1,x2,y2):
    # print('values taken into euclidean_distance:' +str((x1 + 1)) +',' + str((y1 + 1))+ ',' + str(x2)+ ',' + str(y2) )
    return math.sqrt( pow((x1 + 1) - (x2 ),2) + pow( (y1 + 1) - (y2 ), 2))

BLOCKED = 1
UNBLOCKED = 0
HEURISTIC =None
NORTH = 'n'
SOUTH = 's'
EAST = 'e'
WEST = 'w'
STUCK  = 'stuck'

OPEN_LIST = []
RED_LIST = set()
CLOSED_LIST = []
CLOSED_LIST_BACKTRACK = []






def main():
    global HEURISTIC
    if (sys.argv[1] == 'e'):
        HEURISTIC =euclidean_distance
    elif(sys.argv[1] == 'm'):
        HEURISTIC = manhattan_distance
    elif(sys.argv[1] == 'c'):
        HEURISTIC = chebyshev_distance
    DIM = int(sys.argv[2])
    p = float(sys.argv[3])
    run_this_many_times = int(sys.argv[4])
    data = []
    how_many_solved  = 0
    start = time.time()
    for times in range(run_this_many_times):
        print(f'TEST #{times+1}')
        g =  generate_grid(DIM, p)
        grid_result =  (times, A_Star_Search(g, (0,0), DIM))
        data.append(grid_result)
        if(grid_result[1]):
            how_many_solved += 1
    end = time.time()
    print(f"{how_many_solved}/{run_this_many_times} grids were solved with a probability of {p} on a {DIM}X{DIM} grid  in {round(end - start,2)} seconds" )

    return grid_result




def get_cost_element(element):
    # print('element:' + str(element[2]))
    return element[2]




def get_legal_moves(x,y,dim, Grid):
    possible_moves = find_potential_moves(x,y)
    legal_moves  = []
    for move in possible_moves:
        if(check_bounds(move[0],move[1], dim)):
                legal_moves.append(move)

    return legal_moves

def check_bounds(x,y,dim):
    return (x >= 0 and x<dim) and (y >= 0 and y<dim)

def find_potential_moves(x,y):
    # print(x,y)
    # print('returning:' + str(((x-1,y),(x+1,y),(x,y-1),(x,y+1))))
    return ((x-1,y),(x+1,y),(x,y-1),(x,y+1))




def sort_paths(path_list):
    path_list.sort(key=get_cost_element)

def calc_cost(x,y,dim):
    return (HEURISTIC(x,y,dim,dim))


def make_move(Grid,current_agent_position, DIM ):
    make_return = False
    # print('current_agent_position:', current_agent_position)
    # print('OPEN_LIST before path loop~~~~~~~:', OPEN_LIST)
    # print('CLOSED_LIST before path loop:', CLOSED_LIST)
    # print('RED_LIST before path loop:', RED_LIST)
    for path in OPEN_LIST:
        # print('path in OPEN_LIST loop--->>>>>:', path)
        if ( (Grid[path[0]][path[1]] != BLOCKED) and (not((path[0], path[1]) in RED_LIST)) and (not((path[0], path[1]) in CLOSED_LIST)) ):
            # print('move args:', (current_agent_position[0],current_agent_position[1],path[0], path[1], Grid))
            CLOSED_LIST.append( ( current_agent_position[0],current_agent_position[1] ))
            # print('Haha')
            CLOSED_LIST_BACKTRACK.append(current_agent_position)
            # print('Haha')
            move(current_agent_position[0],current_agent_position[1],path[0], path[1], Grid )
            # print('Haha')
            current_agent_position = (path[0], path[1])
            # print('Haha')
            make_return = True
            # print('Haha')
            break
    for path in OPEN_LIST:
        if (Grid[path[0]][path[1]] == BLOCKED):
            RED_LIST.add((path[0],path[1]))
    OPEN_LIST.clear()
    # print('new current_agent_positions@@@@@:' ,(current_agent_position[0],current_agent_position[1], DIM, Grid))
    legal_moves = get_legal_moves(current_agent_position[0],current_agent_position[1], DIM, Grid )
    # print('legal_moves: ' + str(legal_moves))
    for legal_move in legal_moves:
        cost = calc_cost(legal_move[0],legal_move[1], DIM)
        OPEN_LIST.append(  ( legal_move[0],legal_move[1],cost)   )
        # print('OPEN_LIST from move function:', OPEN_LIST)
    sort_paths(OPEN_LIST)

    # print('SORTED PATHS######:', OPEN_LIST)
    return (make_return, current_agent_position)

def A_Star_Search(Grid,S,DIM):
        global OPEN_LIST
        global RED_LIST
        global CLOSED_LIST
        global CLOSED_LIST_BACKTRACK
        OPEN_LIST = []
        RED_LIST = set()
        CLOSED_LIST = []
        CLOSED_LIST_BACKTRACK = []
        cost = 0
        x_destination =  S[0]
        y_destination = S[1]
        current_agent_position = (x_destination,y_destination)
        legal_moves = get_legal_moves(x_destination,y_destination, DIM, Grid )
        # print('legal_moves: ' + str(legal_moves))
        for legal_move in legal_moves:
            cost = calc_cost(legal_move[0],legal_move[1], DIM)
            OPEN_LIST.append(  ( legal_move[0],legal_move[1],cost)   )
        sort_paths(OPEN_LIST)
        count = 0
        while(Grid[DIM-1][DIM-1] ==  'G'):
            # print('Current count:', count)
            if(len(OPEN_LIST)!=0):
                # print('OPEN LIST has something', OPEN_LIST)
                return_val  =  make_move(Grid, current_agent_position, DIM)
                # print('OPEN LIST HAS SOMETHING AFTER>>>>>')
                current_agent_position = return_val[1]
                # print('OPEN LIST HAS SOMETHING AFTER>>>>>#2')
                return_val_bol  = return_val[0]
                # print('OPEN LIST HAS SOMETHING AFTER>>>>>#3')
                # print('************************returning tuple from make_move***********', return_val)
                if(not(return_val_bol)):
                    # print('OPEN LIST HAS SOMETHING AFTER>>>>>#5')
                    if(len(CLOSED_LIST_BACKTRACK) != 0):
                        RED_LIST.add(current_agent_position)
                        last_move = CLOSED_LIST_BACKTRACK.pop()
                        move(current_agent_position[0], current_agent_position[1], last_move[0], last_move[1], Grid)
                        current_agent_position =  (last_move[0], last_move[1])
                        OPEN_LIST.clear()
                        # print('new current_agent_positions@@@@@:' ,(current_agent_position[0],current_agent_position[1], DIM, Grid))
                        legal_moves = get_legal_moves(current_agent_position[0],current_agent_position[1], DIM, Grid )
                        # print('legal_moves: ' + str(legal_moves))
                        for legal_move in legal_moves:
                            cost = calc_cost(legal_move[0],legal_move[1], DIM)
                            OPEN_LIST.append(  ( legal_move[0],legal_move[1],cost)   )
                            # print('OPEN_LIST from move function:', OPEN_LIST)
                            sort_paths(OPEN_LIST)
                    else:
                        print('The agent is stuck here:')
                        # print('current_agent_position:', current_agent_position)
                        print_grid(Grid)
                        return False
            else:
                print('There is no path between agent and goal:')
                print_grid(Grid)
                return False
            count += 1
        return True


            # if(count>25):
                # break













def manhattan_distance(x1,y1,x2,y2):
    return abs( (x1 + 1) - (x2 + 1) ) + abs( (y1 + 1) - (y2 + 1))

def chebyshev_distance(x1,y1,x2,y2):
    """
    This function is also known as chess distance. That means how many moves it'll
    take the king to move from (x1,y1) to (x2,y2), if the grid were a chess board.
    """
    return max(abs((x1 + 1) - (x2 + 1) ), abs( (y1 + 1) - (y2 + 1)))


def calc_north_cost(S, dim):
    return(S[0] - 1, S[1], HEURISTIC(S[0] - 1, S[1], dim, dim))

def calc_south_cost(S, dim):
    # print('values being passed to HEURISTIC:' + str((int(S[0]), int(S[1])) ))
    # print('calc_south_cost:' +  str(S)+ str(dim))
    return(int(S[0]) + 1, int(S[1]) , HEURISTIC(int(S[0]) + 1, int(S[1] ), dim, dim))

def calc_west_cost(S, dim):
    return(S[0], S[1] - 1, HEURISTIC(S[0], S[1] - 1, dim, dim))

def calc_east_cost(S, dim):
    return(int(S[0]), S[1] + 1, HEURISTIC(S[0], S[1] + 1, dim, dim))

def check_red_north(X, Y):
    if ( (X-1, Y) == 1):
        RED_LIST.add( X-1, Y)



def check_red_south(X, Y):
    if( (X+1, Y) == 1):
        RED_LIST.add( X+1, Y)



def check_red_west(X, Y):
    if( (X, Y-1) == 1):
        RED_LIST.add( X, Y-1)


def check_red_east(X, Y):
    if ( (X, Y+1) == 1):
        RED_LIST.add( X, Y+1)


def move(source_x,source_y, x_destination, y_destination,G):
    # print('move args:', (source_x,source_y, x_destination, y_destination,G))
    G[source_x][source_y], G[x_destination][y_destination] = G[x_destination][y_destination], G[source_x][source_y]
    print_grid(G)



#
#
#
# def move_agent_north(grid, agent_position):
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     grid[x_agent_position][y_agent_position], grid[x_agent_position-1][y_agent_position]  = grid[x_agent_position- 1], grid[y_agent_position], grid[x_agent_position][y_agent_position]
#     print_grid(grid)
#
# def move_agent_south(grid, agent_position):
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     grid[x_agent_position][y_agent_position], grid[x_agent_position+1][y_agent_position]  = grid[x_agent_position+ 1][y_agent_position], grid[x_agent_position][y_agent_position]
#     print_grid(grid)
#
# def move_agent_east(grid, agent_position):
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     grid[x_agent_position][y_agent_position], grid[x_agent_position][y_agent_position+1]  = grid[x_agent_position][y_agent_position+1], grid[x_agent_position][y_agent_position]
#     print_grid(grid)
#
#
# def move_agent_west(grid, agent_position):
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     grid[x_agent_position][y_agent_position], grid[x_agent_position][y_agent_position-1]  = grid[x_agent_position][y_agent_position-1], grid[x_agent_position][y_agent_position]
#     print_grid(grid)
#
# def look_and_tell_south_cell(grid,agent_position):
#     """
#     Looks and tell if the south cell, relative to agent_position, is blocked or not.
#     If it is unblocked, this function returns True. If it is blocked, it returns false.
#     """
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     return grid[x_agent_position+1][y_agent_position]==UNBLOCKED
#
# def look_and_tell_north_cell(grid,agent_position):
#     """
#     Looks and tell if the north cell, relative to agent_position, is blocked or not.
#     If it is unblocked, this function returns True. If it is blocked, it returns false.
#     """
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     return grid[x_agent_position-1][y_agent_position]==UNBLOCKED
#
# def look_and_tell_east_cell(grid,agent_position):
#     """
#     Looks and tell if the east cell, relative to agent_position, is blocked or not.
#     If it is unblocked, this function returns True. If it is blocked, it returns false.
#     """
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     return grid[x_agent_position][y_agent_position+1]==UNBLOCKED
#
# def look_and_tell_west_cell(grid,agent_position):
#     """
#     Looks and tell if the west cell, relative to agent_position, is blocked or not.
#     If it is unblocked, this function returns True. If it is blocked, it returns false.
#     """
#     x_agent_position = agent_position[0]
#     y_agent_position = agent_position[1]
#     return grid[x_agent_position][y_agent_position-1]==UNBLOCKED

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



main()
