import heapq
import numpy as np

from grid import GridWorld
from utils import stateNameToCoords
from d_star_lite_3d import initDStarLite, moveAndRescan
from graph import Node, Graph



# Create a 10x10 3 dimensional array.
grid = np.zeros((10,10,10))


#for cell in range(10):
#    grid.append([])
#    for row in range(10):
#        # Add an empty array that will hold each cell
#        # in this row
#        grid.append([])
#        for column in range(10):
#            grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][1][1] = 1

done = False


if __name__ == "__main__":

    
#    s_start = 'x1y2z3'
#    s_goal = 'x5y4z5'
    
    world = input("Enter world size (X_size,Y_size,Z_size): " + '\n')
    world = world.split(',')
    
    print("Enter X,Y,Z coordinates like as (1,2,3)" + '\n')
    start = input("Enter starting position: ")
    start = start.split(',')
    
    goal = input("Enter goal position: ")
    goal = goal.split(',')
    
    

    
    
    s_start = [int(x) for x in start]
    s_goal = [int(x) for x in goal]
    worldSize = [int(x) for x in world]
    
    graph = GridWorld(worldSize[0], worldSize[1], worldSize[2])

    

    graph.setStart(s_start)
    graph.setGoal(s_goal)
    k_m = 0
    s_last = s_start
    queue = []

    graph, queue, k_m = initDStarLite(graph, queue, s_start, s_goal, k_m)

    s_current = s_start
    pos_coords = stateNameToCoords(s_current)

    
    # -------- Main Program Loop -----------
    
    while not done:
        s_new, k_m = moveAndRescan(graph, queue, s_current, k_m)
    
### Unused loop for PyGame
    
#    while not done:
#        for event in pygame.event.get():  # User did something
#            if event.type == pygame.QUIT:  # If user clicked close
#                done = True  # Flag that we are done so we exit this loop
#            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#                # print('space bar! call next action')
#                s_new, k_m = moveAndRescan(graph, queue, s_current, k_m)
#                if s_new == 'goal':
#                    print('Goal Reached!')
#                    done = True
#                else:
#                    # print('setting s_current to ', s_new)
#                    s_current = s_new
#                    pos_coords = stateNameToCoords(s_current)
#                    # print('got pos coords: ', pos_coords)


