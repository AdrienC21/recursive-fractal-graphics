import numpy as np
import matplotlib.pyplot as plt


nbiter = 8  # number of iterations
size = 3**7  # size of the array


def sponge(n, m):
    """Plot the menger sponge (mxm matrix) with n iterations

    Args:
        n (int): number of iterations
        m (int): matrix size
    """
    M = np.zeros((m, m))

    def trouer(n, xa, ya, xb, yb):
        """Insert a hole between (xa, ya) and (xb, yb)
        Then iterate n-1 itself inside

        Args:
            n (int): number of iterations
            xa (float): x coordinate of A
            ya (float): y coordinate of A
            xb (float): x coordinate of B
            yb (float): y coordinate of B
        """
        if n > 0:
            stepx = (xb - xa) // 3
            stepy = (yb - ya) // 3
            for i in range(xa + stepx, xa + 2 * stepx):
                for j in range(ya + stepy, ya + 2 * stepy):
                    M[i][j] = 1
            trouer(n - 1, xa, ya, xa + stepx, ya + stepy)
            trouer(n - 1, xa + stepx, ya, xa + 2 * stepx, ya + stepy)
            trouer(n - 1, xa + 2 * stepx, ya, xb, ya + stepy)
            trouer(n - 1, xa, ya + stepy, xa + stepx, ya + 2 * stepy)
            trouer(n - 1, xa + 2 * stepx, ya + stepy, xb, ya + 2 * stepy)
            trouer(n - 1, xa, ya + 2 * stepy, xa + stepx, yb)
            trouer(n - 1, xa + stepx, ya + 2 * stepy, xa + 2 * stepx, yb)
            trouer(n - 1, xa + 2 * stepx, ya + 2 * stepy, xb, yb)
    trouer(n, 0, 0, m, m)
    plt.matshow(M)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


sponge(nbiter, size)
