"""
projet PyChess

-> point d'entrée du programme
"""

# | librairies


# | fichiers de projet
from game import *


def main():
    """ fonction d'entrée
    """
    grid = init_grid()
    for i in range(8):
        print("  ".join(grid[i]))

if __name__ == "__main__":
    main()
