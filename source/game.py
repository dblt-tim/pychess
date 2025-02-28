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

    def move(self, from_pos, to_pos):
        """
        1. on vérifie si le roi n'est pas en échec
            -> si il est en échec à 2.
            -> sinon à 3.
        2. on vérifie si il est en échec et mat
            -> si oui, fin de la partie et victoire de l'adversaire
            -> sinon chercher les coups légaux pour sortir le roi de l'échec
        3. on vérifie si le pion demandé peut faire le mouvement demandé
        4. on vérifie si le mouvement demandé ne met pas le roi en échec

        Conditions de roque :
        1. le roi et la tour cible ne doivent pas avoir bougé depuis le début de la partie
        2. il ne doit pas y avoir de pion entre les deux
        3. le roi ne doit pas être en échec
        4. le roi ne doit pas arriver en position d'échec
        """
        
