from turtle import *
import turtle as turtle
import numpy as np
import random as rd
from math import *

sizepolygon = 7  # size of a vertice of an hexagon
size = 94  # size of the grid
p = 0.6  # Between 0 and 1. Hole creation probability


def polygon(size, col):
    """Draw one hexagon

    Args:
        size (int): size of a vertice of the hexagon
        col ([type]): [description]
    """
    n = 6
    angle = 60
    color(col, col)
    begin_fill()
    for x in range(n):
        forward(size)
        left(angle)
    end_fill()


def creation_grid_hex(p, n):
    """Create an hexagonal grid of size n
    p is the probability of a hole to appear
    The grid is a 2D array with a sequence of n and n-1 values
    (to simulate the hexagonal shape)

    Args:
        p (float): between 0 and 1. Probability of creating a hole
        n (int): size of the matrix. n must be EVEN and GREATER THAN 4 !
    """
    if n < 3 or n % 2 != 0:
        raise ValueError("n must be greater or equal than 4 "
                         "and must be even !")
    tab = np.zeros((n, n))
    for i in range(n):
        if i % 2 == 0:
            m = n - 1
        else:
            m = n
        for j in range(m):
            a = rd.random()
            if a <= p:
                tab[i][j] = 1.0  # hole color
            else:
                tab[i][j] = 2.0  # new wall color
    return tab


def percolationhex(tab):
    """Perform the percolation on an hexagonal grid

    Args:
        tab (array): array created by creation_grid_hex
    """
    n = len(tab)
    pile = []
    for j in range(n):
        if tab[0][j] == 1.0:
            pile.append((0, j))
    while pile != []:
        (i, j) = pile.pop()
        tab[i][j] = 0.5  # hole color
        if i > 1:
            if i % 2 == 0:
                if tab[i - 2][j] == 1.0:
                    pile.append((i - 2, j))
                if tab[i - 1][j] == 1.0:
                    pile.append((i - 1, j))
                if tab[i - 1][j + 1] == 1.0:
                    pile.append((i - 1, j + 1))
            else:
                if j == 0:
                    if tab[i - 2][j] == 1.0:
                        pile.append((i - 2, j))
                    if tab[i - 1][j] == 1.0:
                        pile.append((i - 1, j))
                elif j == n - 1:
                    if tab[i - 2][j] == 1.0:
                        pile.append((i - 2, j))
                    if tab[i - 1][j - 1] == 1.0:
                        pile.append((i - 1, j - 1))
                else:
                    if tab[i - 2][j] == 1.0:
                        pile.append((i - 2, j))
                    if tab[i - 1][j - 1] == 1.0:
                        pile.append((i - 1, j - 1))
                    if tab[i - 1][j] == 1.0:
                        pile.append((i - 1, j))
        if i < n - 2:
            if i % 2 == 0:
                if tab[i + 2][j] == 1.0:
                    pile.append((i + 2, j))
                if tab[i + 1][j] == 1.0:
                    pile.append((i + 1, j))
                if tab[i + 1][j + 1] == 1.0:
                    pile.append((i + 1, j + 1))
            else:
                if j == 0:
                    if tab[i + 2][j] == 1.0:
                        pile.append((i + 2, j))
                    if tab[i + 1][j] == 1.0:
                        pile.append((i + 1, j))
                elif j == n - 1:
                    if tab[i + 2][j] == 1.0:
                        pile.append((i + 2, j))
                    if tab[i + 1][j - 1] == 1.0:
                        pile.append((i + 1, j - 1))
                else:
                    if tab[i + 2][j] == 1.0:
                        pile.append((i + 2, j))
                    if tab[i + 1][j - 1] == 1.0:
                        pile.append((i + 1, j - 1))
                    if tab[i + 1][j] == 1.0:
                        pile.append((i + 1, j))
        if i == 0:
            if tab[i + 2][j] == 1.0:
                pile.append((i + 2, j))
            if tab[i + 1][j] == 1.0:
                pile.append((i + 1, j))
            if tab[i + 1][j + 1] == 1.0:
                pile.append((i + 1, j + 1))
        if i == 1:
            if j == 0:
                if tab[i - 1][j] == 1.0:
                    pile.append((i - 1, j))
                if tab[i + 1][j] == 1.0:
                    pile.append((i + 1, j))
                if tab[i + 2][j] == 1.0:
                    pile.append((i + 2, j))
            elif j == n - 1:
                if tab[i - 1][j - 1] == 1.0:
                    pile.append((i - 1, j - 1))
                if tab[i + 1][j - 1] == 1.0:
                    pile.append((i + 1, j - 1))
                if tab[i + 2][j] == 1.0:
                    pile.append((i + 2, j))
            else:
                if tab[i + 2][j] == 1.0:
                    pile.append((i + 2, j))
                if tab[i - 1][j] == 1.0:
                    pile.append((i - 1, j))
                if tab[i - 1][j + 1] == 1.0:
                    pile.append((i - 1, j + 1))
                if tab[i + 1][j] == 1.0:
                    pile.append((i + 1, j))
                if tab[i + 1][j + 1] == 1.0:
                    pile.append((i + 1, j + 1))
        if i == n - 1:
            if j == 0:
                if tab[i - 2][j] == 1.0:
                    pile.append((i - 2, j))
                if tab[i - 1][j] == 1.0:
                    pile.append((i - 1, j))
            elif j == n - 1:
                if tab[i - 2][j] == 1.0:
                    pile.append((i - 2, j))
                if tab[i - 1][j - 1] == 1.0:
                    pile.append((i - 1, j - 1))
            else:
                if tab[i - 2][j] == 1.0:
                    pile.append((i - 2, j))
                if tab[i - 1][j] == 1.0:
                    pile.append((i - 1, j))
                if tab[i - 1][j + 1] == 1.0:
                    pile.append((i - 1, j + 1))
        if i == n - 2:
            if tab[i - 2][j] == 1.0:
                pile.append((i - 2, j))
            if tab[i - 1][j] == 1.0:
                pile.append((i - 1, j))
            if tab[i - 1][j + 1] == 1.0:
                pile.append((i - 1, j + 1))
            if tab[i + 1][j] == 1.0:
                pile.append((i + 1, j))
            if tab[i + 1][j + 1] == 1.0:
                pile.append((i + 1, j + 1))


def coloration(i, j, tab):
    """Return the color associate to a value on the grid
    given the coordinates

    Args:
        i (int): row index
        j (int): column index
        tab (array): hexagonal grid

    Returns:
        str: return a color associate to a given hexagon
    """
    if tab[i][j] == 0.5:  # liquid color
        return "#33b2cc"
    elif tab[i][j] == 1.0:  # hole color
        return "#ffffff"
    elif tab[i][j] == 2.0:  # wall color
        return "#000000"
    else:
        return "#8c8c8c"  # color of other blocks


def drawhex(tab, size):
    """Draw the grid after percolation (tab) with hexagon size equal to size

    Args:
        tab (array): Grid after percolation
        taille (float): size of a vertice
    """

    (x, y) = (-960 + size * cos(pi / 6), 515 - size * sin(pi / 6))
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    n = len(tab)
    i = 0
    while i < n:
        if i % 2 == 0:
            for j in range(n - 1):
                c = coloration(i, j, tab)
                polygon(size, c)
                turtle.penup()
                turtle.forward(size)
                turtle.left(60)
                turtle.forward(size)
                turtle.right(60)
                turtle.forward(size)
                turtle.right(60)
                turtle.forward(size)
                turtle.left(60)
                turtle.pendown()
            turtle.penup()
            turtle.setx(x)
            turtle.sety(y)
            turtle.left(240)
            turtle.forward(size)
            turtle.right(60)
            turtle.forward(size)
            turtle.right(180)
            turtle.pendown()
            (x, y) = turtle.pos()
        else:
            for j in range(n):
                c = coloration(i, j, tab)
                polygon(size, c)
                turtle.penup()
                turtle.forward(size)
                turtle.left(60)
                turtle.forward(size)
                turtle.right(60)
                turtle.forward(size)
                turtle.right(60)
                turtle.forward(size)
                turtle.left(60)
                turtle.pendown()
            turtle.penup()
            turtle.setx(x)
            turtle.sety(y)
            turtle.forward(size)
            turtle.right(60)
            turtle.forward(size)
            turtle.left(60)
            turtle.pendown()
            (x, y) = turtle.pos()
        i = i + 1


def draw_hexagonal_percolation(sizepolygon, size, p):
    """Combine all the previous functions to creata grid,
    perfom the percolation, draw

    Args:
        sizepolygon (int): size of a vertice of an hexagon
        size (int): size of the grid
        p (float): Between 0 and 1. Hole creation probability
    """
    tab = creation_grid_hex(p, size)
    percolationhex(tab)
    drawhex(tab, sizepolygon)


# turtle.speed(0)
turtle.hideturtle()
turtle.tracer(2, 100)
draw_hexagonal_percolation(sizepolygon, size, p)
