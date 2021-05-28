import numpy as np
import matplotlib.pyplot as plt
import random as rd


proba = 0.6  # probability of a hole to a appear when building grid
size = 100  # size of the matrix


def grid_creation(p, n):
    """Create a grid

    Args:
        p (float): between 0 and 1. Probability of creating a hole
        n (int): size of the matrix

    Returns:
        array: n by n square with holes
    """
    tab = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            a = rd.random()
            if a <= p:
                tab[i][j] = 1.0
    return tab


def percolation(tab):
    """Perform a percolation on tab

    Args:
        tab (array): Array of 0 and 1. (1 are holes, 0 are walls)
    """
    n = len(tab)
    pile = []
    for j in range(n):  # fill first holes with a liquid
        if tab[0][j] == 1.0:
            pile.append((0, j))
    while pile != []:  # propagation of the fluid
        (i, j) = pile.pop()
        tab[i][j] = 0.5  # fluid color
        if i > 0 and tab[i - 1][j] == 1.0:
            pile.append((i - 1, j))
        if j > 0 and tab[i][j - 1] == 1.0:
            pile.append((i, j - 1))
        if j < n - 1 and tab[i][j + 1] == 1.0:
            pile.append((i, j + 1))
        if i < n - 1 and tab[i + 1][j] == 1.0:
            pile.append((i + 1, j))


tab = grid_creation(proba, size)
percolation(tab)
plt.matshow(tab)
plt.axis('equal')
plt.axis('off')
plt.show()

print("Calculating percolation probabilities ...")


def test_percolation(p, n):
    """Create a grid, perform a percolation, check if it succeeded

    Args:
        p (float): between 0 and 1. Probability of creating a hole
        n (int): size of the matrix

    Returns:
        bool: if True, the percolation has reached the bottom
    """
    tab = grid_creation(p, n)
    percolation(tab)
    perco = False
    k = 0
    n = len(tab)
    while not(perco) and k < n:
        perco = (tab[n - 1][k] == 0.5)
        k = k + 1
    return perco


def proba(p, n, N):
    """Return the probability that a percolation will succeed for
    the given parameters p and n

    Args:
        p (float): between 0 and 1. Probability of creating a hole
        n (int): size of the matrix
        N (int): number of times we make a simulation

    Returns:
        float: probability that a percolation will succeed
    """
    S = 0
    for _ in range(N):
        test = test_percolation(p, n)
        if test:
            S = S + 1
    return S / N


"""
Cut the segment [0,1] in 26 elements, run 100 simulations on a 100x100 matrix
to return a probability that the percolation reach the botton in function of
a given hole creation probability p.
"""
h = 1/25
x = 0
X = [0]
for k in range(25):
    x = x + h
    X.append(x)
Y = [proba(p, 100, 100) for p in X]
Y = np.array(Y)
plt.plot(X, Y, label='proba(p,n=100,N=100)')
plt.xlabel("Hole probability p")
plt.ylabel("Probability that percolation succeed")
plt.title("Probability that a percolation reach the bottom : n=100, N=100")
plt.legend(loc='best')
plt.show()

print("Calculating percolation density ...")


def density(tab):
    """Return for a given grid the proportion of filled holes among all holes
    after percolation

    Args:
        tab (array): grid

    Returns:
        float: proportion of filled holes
    """
    n = len(tab)
    holes = 0
    filled = 0
    for i in range(n):
        for j in range(n):
            if tab[i][j] == 1.0:
                holes = holes + 1
            elif tab[i][j] == 0.5:
                filled = filled + 1
                holes = holes + 1
    if holes == 0:
        return 0
    else:
        return filled / holes


def d(p):
    """Based on 20 simulations on a 100 by 100 matrix, return an average
    density in function of p

    Args:
        p (float): hole creation probability

    Returns:
        float: expected density
    """
    res = 0
    for _ in range(20):
        tab = grid_creation(p, 100)
        percolation(tab)
        res = res + density(tab)
    return res / 20


"""
Cut the segment [0,1] in 26 elements, run 20 simulations on a 100x100 matrix
to calculate the average density of filled holes after percolation in
function of a given hole creation probability p.
"""

X = np.linspace(0, 1, 26)  # 26 points
Y = [d(p) for p in X]
plt.plot(X, Y, label='Density')
plt.xlabel("Hole probability p")
plt.ylabel("Expected proportion of filled holes")
plt.title("Density of filles holes : n=100")
plt.legend(loc='best')
plt.show()
