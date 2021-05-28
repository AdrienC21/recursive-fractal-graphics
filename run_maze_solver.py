import matplotlib.pyplot as plt
import random as rd
from copy import deepcopy

n = 9  # size of the n*n maze
p = 0.6  # probability of creating a land instead of a wall in our maze
# Random initial and final coordinates
initial_coordinate = (rd.randint(0, n - 1), rd.randint(0, n - 1))
final_coordinate = (rd.randint(0, n - 1), rd.randint(0, n - 1))


def createMaze(n, p):
    """Create a random maze of size n with a land creation probability p

    Args:
        n (int): size of the n*n maze
        p (float): probability of creating a land instead of a wall
        in our maze. Between 0 and 1

    Returns:
        list: maze (2D list)
    """
    return [[1 if rd.random() < p else 0 for i in range(n)] for j in range(n)]


def visitable(coord, maze):
    """Check if a coordinate is at first sight visitable

    Args:
        coord (tuple): tuple of two integers
        maze (list): maze

    Returns:
        bool: is the coordinate in the maze visitable
    """
    x, y = coord
    n = len(maze)
    if x >= 0 and x < n and y >= 0 and y < n:
        return (maze[x][y] == 1)
    else:
        return False


def visit(coord, arrival, maze, mbool, path):
    """Recursively explore the maze from coordinate coord searching for
    arrival. Store the path explored from now in path and the visited
    coordinates in mbool


    Args:
        coord (tuple): current coordinates in the maze
        arrival (tuple): coordinates we want to reach
        maze (list): maze
        mbool (list): list of booleans (if True, the coord has been visited)
        path (list): list of explored coordinates from now on

    Returns:
        bool, list, list: if we found the arrival, the list of all the explored
        coordinates, the path used from the beginning.
    """
    x, y = coord
    ax, ay = arrival
    n = len(maze)
    mbool[x][y] = True  # we explore this coordinate
    neighb = []  # we add the neighbors not yet visited
    for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if visitable((x + i, y + j), maze) and not(mbool[x + i][y + j]):
            neighb.append((x + i, y + j))
    for coord_neighb in neighb:  # for each neighbors
        path_final = deepcopy(path)
        path_final.append(coord_neighb)
        mboolneighb = deepcopy(mbool)
        xneighb, yneighb = coord_neighb
        mboolneighb[xneighb][yneighb] = True
        if ax == xneighb and ay == yneighb:  # if neighbors has arrived
            return True, mboolneighb, path_final
        else:  # not yet visited so we explore it
            arrival_found, mbool_mod,\
                path_mod = visit(coord_neighb, arrival, maze, mboolneighb,
                                 path_final)
            if arrival_found:  # if arrival found
                return arrival_found, mbool_mod, path_mod
    return mbool[ax][ay], mbool, path


def pathExists(departure, arrival, maze):
    """Check if a path in the maze exists between the coordinates
    departure and arrival. If so, return the the explored cases
    and the total path.

    Args:
        departure (tuple): initial coordinates
        arrival (tuple): coordinates we want to reach
        maze (list): maze

    Returns:
        bool, list, list: if we found the arrival, the list of all the explored
        coordinates, the path used from the beginning.
    """
    n = len(maze)
    mbool = [[False for i in range(n)] for j in range(n)]
    initialPath = [departure]
    found, mat, path = visit(departure, arrival, maze, mbool, initialPath)
    return found, mat, path


print("Creation of the maze ...")
maze = createMaze(n, p)
print("Finding a path")
b, mat, path = pathExists(initial_coordinate, final_coordinate, maze)

plt.matshow(maze)
plt.title("Initial maze")
plt.axis("equal")
plt.axis("off")
plt.show()
if b:
    print("Arrival found !")
else:
    print("Arrival not found ...")
print("Path : {path}".format(path=path))
plt.matshow(mat)
plt.title("Coordinates explored")
plt.axis("equal")
plt.axis("off")
plt.show()
