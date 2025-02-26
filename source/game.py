"""
projet PyChess
-> code relatif à une partie
"""

# | librairies
import random



def init_grid():
    """ fonction de génération d'un plateau
    """
    grid : list[list[str]] = [["" for i in range(8)] for j in range(8)]
    pawns = "RNBQKBNR"
    grid[0] = ["b"+ i for i in pawns]
    grid[1] = ["bP" for i in range(8)]
    grid[6] = ["wP" for i in range(8)]
    grid[7] = ["w"+i for i in pawns]
    return grid

class Game:
    """ classe de base où résidera une partie
    """
    def __init__(self, time: int, player1: str, player2: str):
        """ fonction __init__ appartenant à Game :
        paramètres:
         - time : définit le temps (en secondes) donné aux joueurs
         - player1 : nom du premier joueur
         - player2 : nom du deuxième joueur
        """
        self.grid = init_grid()
        self.moves : list["str"] = [] # log des coups joués par les joueurs
        
        # on définit aléatoirement quel joueur commence (en jouant donc les blancs)
        self.wplayer, self.bplayer = random.shuffle([player1, player2])

        
