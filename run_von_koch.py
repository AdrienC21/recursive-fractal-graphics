from math import *
import numpy as np
import matplotlib.pyplot as plt

initial_P1 = np.array([0, 0])  # first coordinate of the initial segment
initial_P2 = np.array([3, 3])  # second coordinate of the initial segment
nbiter = 8  # number of iterations


def tiers(A, B):
    """Add a fractal step

    Args:
        A (array): point in 2D space
        B (array): point in 2D space

    Returns:
        C, D, E: 3 new points in 2D space
    """
    step = (B - A) / 3
    C = A + step
    E = C + step
    rotation = np.array([[cos(pi / 3), -sin(pi / 3)],
                         [sin(pi / 3), cos(pi / 3)]])
    D = np.dot(rotation, (E - C)) + C
    return C, D, E


def fractal(n, A, B):
    """Calculate all the new points added by cutting our segment [A,B] n times

    Args:
        n (int): number of iterations
        A (array): point in 2D space
        B (array): point in 2D space

    Returns:
        list: List of all the points (array)
    """
    L = [A]

    def iteration(n, A, B):
        if n > 0:
            (C, D, E) = tiers(A, B)
            iteration(n - 1, A, C)
            L.append(C)
            iteration(n - 1, C, D)
            L.append(D)
            iteration(n - 1, D, E)
            L.append(E)
            iteration(n - 1, E, B)
    iteration(n, A, B)
    L.append(B)
    return L


def snowflake(n, A, B):
    """Plot the Helge von Koch snowflake

    Args:
        n (int): number of iteration
        A (array): point in 2D space
        B (array): point in 2D space
    """
    rotationC = np.array([[cos(pi / 3), -sin(-pi / 3)],
                          [sin(-pi / 3), cos(pi / 3)]])
    C = np.dot(rotationC, (B - A)) + A
    L = fractal(n, A, B) + fractal(n, B, C) + fractal(n, C, A)
    n = len(L)
    plt.axis('equal')
    plt.axis('off')
    absciss = []
    ordonate = []
    for k in range(0, n):
        absciss.append(L[k][0])
        ordonate.append(L[k][1])
    plt.plot(absciss, ordonate)
    plt.show()


snowflake(nbiter, initial_P1, initial_P2)
