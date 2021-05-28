from math import *
import numpy as np
from copy import deepcopy
import tkinter


M1 = np.array([[0, 1, 0, 0, 5, 2, 0, 0, 7],
               [0, 8, 0, 7, 0, 0, 0, 1, 0],
               [9, 0, 2, 0, 6, 1, 5, 0, 0],
               [4, 0, 0, 2, 0, 0, 7, 0, 0],
               [8, 0, 1, 0, 7, 0, 2, 0, 4],
               [0, 0, 7, 0, 0, 5, 0, 0, 9],
               [0, 0, 6, 5, 3, 0, 9, 0, 8],
               [0, 9, 0, 0, 0, 4, 0, 5, 0],
               [2, 0, 0, 9, 8, 0, 0, 7, 0]])

M2 = np.array([[0, 6, 0, 0, 0, 0, 9, 8, 5],
               [0, 0, 5, 6, 0, 9, 0, 0, 0],
               [0, 0, 7, 0, 0, 0, 0, 4, 0],
               [0, 2, 0, 9, 0, 0, 0, 0, 8],
               [0, 7, 0, 5, 0, 1, 0, 6, 0],
               [1, 0, 0, 0, 0, 3, 0, 9, 0],
               [0, 1, 0, 0, 0, 0, 4, 0, 0],
               [0, 0, 0, 3, 0, 6, 8, 0, 0],
               [6, 5, 9, 0, 0, 0, 0, 1, 0]])

M3 = np.array([[0, 0, 0, 3, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 3, 7, 0],
               [2, 0, 8, 0, 9, 0, 0, 5, 0],
               [6, 9, 0, 0, 0, 2, 0, 0, 0],
               [4, 0, 1, 0, 3, 0, 2, 0, 7],
               [0, 0, 0, 9, 0, 0, 0, 1, 5],
               [0, 1, 0, 0, 7, 0, 8, 0, 3],
               [0, 4, 6, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 4, 0, 3, 0, 0, 0]])


def missingRowi(num, M, i):
    """Search if num is missing from row i of M

    Args:
        num (int): Between 1 and 9
        M (array): sudoku
        i (int): row index

    Returns:
        bool: num is missing from row i of M
    """
    for j in range(9):
        if M[i, j] == num:
            return False
    return True


def missingColumnj(num, M, j):
    """Search if num is missing from column j of M

    Args:
        num (int): Between 1 and 9
        M (array): sudoku
        j (int): column index

    Returns:
        bool: num is missing from column j of M
    """
    for i in range(9):
        if M[i, j] == num:
            return False
    return True


def missingBlockij(num, M, i, j):
    """Search if num is missing from the 3by3 block that contains (i, j)

    Args:
        num (int): Between 1 and 9
        M (array): sudoku
        i (int): row index
        j (int): column index

    Returns:
        bool: num is missing from the 3by3 block that contains (i, j)
    """
    parti = i - i % 3
    partj = j - j % 3
    for i in range(parti, parti + 3):
        for j in range(partj, partj + 3):
            if M[i, j] == num:
                return False
    return True


def test(M, i, j, num):
    """Inserting num in coordinate (i, j) in sudoku M is valid ?

    Args:
        num (int): Between 1 and 9
        M (array): sudoku
        i (int): row index
        j (int): column index

    Returns:
        bool: is the insertion of num valid ?
    """
    return (missingRowi(num, M, i) and missingColumnj(num, M, j) and
            missingBlockij(num, M, i, j))


def isSolvable(M, position):
    """Solve the sudoku M from a certain position
    If it is not solvable, return False.
    Else, solve it by modifying M and return True

    Args:
        M (array): sudoku
        position (int): from 0 to 80, position in the sudoku
        (we solve it row by row)

    Returns:
        bool: is the sudoku solvable
    """
    if position == 9 * 9:
        return True
    i = position // 9
    j = position % 9
    if M[i, j] != 0:
        return isSolvable(M, position + 1)
    for num in range(1, 10):
        if test(M, i, j, num):
            M[i, j] = num
            if isSolvable(M, position + 1):
                return True
    M[i, j] = 0
    return False


def sudoku(M):
    """Solve a copy of the sudoku M, return the sudoku once solved

    Args:
        M (array): sudoku

    Returns:
        array: sudoku
    """
    res = deepcopy(M)
    isSolvable(res, 0)
    return res


def drawSudoku(M):
    top = tkinter.Tk()
    C = tkinter.Canvas(top, bg="white", height=760, width=1400)
    line1 = C.create_line(20, 20, 20, 740, fill="black")
    line2 = C.create_line(100, 20, 100, 740, fill="black")
    line3 = C.create_line(180, 20, 180, 740, fill="black")
    line4 = C.create_line(260, 20, 260, 740, fill="black")
    line5 = C.create_line(340, 20, 340, 740, fill="black")
    line6 = C.create_line(420, 20, 420, 740, fill="black")
    line7 = C.create_line(500, 20, 500, 740, fill="black")
    line8 = C.create_line(580, 20, 580, 740, fill="black")
    line9 = C.create_line(660, 20, 660, 740, fill="black")
    line10 = C.create_line(740, 20, 740, 740, fill="black")

    line11 = C.create_line(20, 20, 740, 20, fill="black")
    line12 = C.create_line(20, 100, 740, 100, fill="black")
    line13 = C.create_line(20, 180, 740, 180, fill="black")
    line14 = C.create_line(20, 260, 740, 260, fill="black")
    line15 = C.create_line(20, 340, 740, 340, fill="black")
    line16 = C.create_line(20, 420, 740, 420, fill="black")
    line17 = C.create_line(20, 500, 740, 500, fill="black")
    line18 = C.create_line(20, 580, 740, 580, fill="black")
    line19 = C.create_line(20, 660, 740, 660, fill="black")
    line20 = C.create_line(20, 740, 740, 740, fill="black")

    for i in range(9):
        for j in range(9):
            C.create_text(i * 80 + 60, j * 80 + 60, text=str(M[i, j]),
                          fill="black", font=("Arial", 35))

    C.create_oval(800, 600, 1240, 160, fill="turquoise", outline="white")
    C.create_text(1020, 380, text="Sudoku Solver", fill="white",
                  font=("Arial", 20))
    C.pack()
    top.mainloop()


drawSudoku(sudoku(M1))
drawSudoku(sudoku(M2))
drawSudoku(sudoku(M3))
