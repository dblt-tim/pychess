"""
PyChess 

"""
def init_grid(): 
    """défini le plateau et setup les pions"""
    grid=[["" for i in range(8)]for j in range(8)]
    grid[0]=["bR","bN","bB","bK","bQ","bB","bN","bR"]
    grid[1]=["bP" for i in range(8)]
    grid[6]=["wP" for i in range(8)]
    grid[7]=["wR","wN","wB","wK","wQ","wB","wN","wR"]
    return grid 
class Game: 
    """classe permettant d'initialiser la partie et de débuter un historique des coups joués """
    def __init__(self):
        self.moves : list[str]  = []
        self.turn : int =0 
        self.grid=init_grid()