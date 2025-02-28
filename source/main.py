"""
projet PyChess

-> point d'entrée du programme
"""

# | librairies


# | fichiers de projet
from game import *
from interface import *

def main():
    """ fonction d'entrée
    """
    grid = init_grid()
    grid_inter=None
    for i in range(8):
        print("  ".join(grid[i]))
        grid_inter=grid_inter+"  ".join(grid[i])
    return grid_inter
if __name__ == "__main__":
    main()
