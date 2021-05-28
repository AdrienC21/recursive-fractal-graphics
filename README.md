# Recursive / Fractals graphics & solvers

A set of different recursive algorithms to solve problems, draw patterns or fractals in python.

## Overview

Here is a list of the different algorithms implemented in this project

- Von Koch Snowflake
- Menger Sponge
- Square percolation (and probability/density analysis)
- Hexagonal percolation
- Sudoku solver
- Maze solver

## Installation

Clone this repository :

```bash
git clone https://github.com/AdrienC21/abm-financial-data.git
```

## How to use

Please find below a short description on how to use each algorithms.

### Von Koch Snowflake

Draw the [Von Koch Snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/von_koch.png?raw=true)

Edit in run_von_koch.py the following lines :

```python
initial_P1 = np.array([0, 0])  # first coordinate of the initial segment
initial_P2 = np.array([3, 3])  # second coordinate of the initial segment
nbiter = 8  # number of iterations
```

Run run_von_koch.py

### Menger Sponge

Draw the [Menger Sponge](https://en.wikipedia.org/wiki/Menger_sponge)

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/sponge.png?raw=true)

Edit in run_menger.py the following lines :

```python
nbiter = 8  # number of iterations
size = 3**7  # size of the array
```

Run run_von_koch.py

### Square percolation

Create a random array with holes and process a percolation from the top. Draw the result.

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/percolation.png?raw=true)

Then, an estimation of the density of filled holes and an estimation of the probability that a percolation on a random array will reach the botton is also plotted.

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/proba.png?raw=true)
![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/density.png?raw=true)

Edit in run_square_percolation.py the following lines :

```python
proba = 0.6  # probability of a hole to a appear when building grid
size = 100  # size of the matrix
```

Run run_square_percolation.py

### Hexagonal percolation

Create a random hexagonal grid with holes and process a percolation from the top. Draw the result.

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/percolation_hex.png?raw=true)

Edit in run_hex_percolation.py the following lines :

```python
sizepolygon = 7  # size of a vertice of an hexagon
size = 94  # size of the grid
p = 0.6  # Between 0 and 1. Hole creation probability
```

Run run_hex_percolation.py

### Sudoku solver

Sudoku solver that use a recursive algorithm. Draw the sudoku once solved.

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/sudoku.png?raw=true)

(OPTIONAL) Edit in run_sudoku_solver.py one of the sudokus :

```python
# Example of a sudoku written in python
M1 = np.array([[0, 1, 0, 0, 5, 2, 0, 0, 7],
               [0, 8, 0, 7, 0, 0, 0, 1, 0],
               [9, 0, 2, 0, 6, 1, 5, 0, 0],
               [4, 0, 0, 2, 0, 0, 7, 0, 0],
               [8, 0, 1, 0, 7, 0, 2, 0, 4],
               [0, 0, 7, 0, 0, 5, 0, 0, 9],
               [0, 0, 6, 5, 3, 0, 9, 0, 8],
               [0, 9, 0, 0, 0, 4, 0, 5, 0],
               [2, 0, 0, 9, 8, 0, 0, 7, 0]])
```

Run run_sudoku_solver.py

### Maze solver

**WARNING :** The algorithm may take a lot of time.

Maze solver that use a recursive algorithm. Draw the maze, the coordinates explored an print the path in the console.

![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/init_maze.png?raw=true)
![alt text](https://github.com/AdrienC21/recursive-fractal-graphics/blob/main/images/path.png?raw=true)

(OPTIONAL) Edit in run_maze_solver.py the following lines :

```python
n = 9  # size of the n*n maze
p = 0.6  # probability of creating a land instead of a wall in our maze
# Random initial and final coordinates
initial_coordinate = (rd.randint(0, n - 1), rd.randint(0, n - 1))
final_coordinate = (rd.randint(0, n - 1), rd.randint(0, n - 1))
```

Run run_maze_solver.py

## License

[MIT](https://choosealicense.com/licenses/mit/)
