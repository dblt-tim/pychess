"""
PyChess 

"""
import random 
import time 
def init_grid(): 
    """défini le plateau et setup les pions"""
    grid=[["" for i in range(8)]for j in range(8)]
    grid[0]=["bR","bN","bB","bK","bQ","bB","bN","bR"]
    grid[1]=["bP" for i in range(8)]
    grid[6]=["wP" for i in range(8)]
    grid[7]=["wR","wN","wB","wK","wQ","wB","wN","wR"]
    return grid 
class Game: 
    """classe permettant d'initialiser la partie et de débuter un historique des coups joués
     les paramètre à prendre en compte:
     -le nom des joueurs (player1 et player2)
     -le timer de base (en seconde)
       """
    def __init__(self,player1 :str, player2 :str, timer : int):
    
        self.moves : list[str]  = [] #historique de la partie
        self.turn : int =0 # initialisation du tour de jeu 
        self.grid=init_grid()


        players : list[str] = random.shuffle([player1,player2])#tirage pour savoir qui va être le joueur blanc et qui va être le joueur noir
        self.white_player=[players[0], timer]
        self.black_player=[players[1], timer]
