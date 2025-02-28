"""
projet PyChess
-> code permettant de créer l'interface pour que les joueurs puissent jouer 
"""
from main import *
from game import *
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage 
board=init_grid()
root=Tk()
frm=ttk.Frame(root)
frm.grid()
for i in range(len(board)):
       for token in board:
            for x in token:
                if  x=='':
                    print("test")
       ttk.Label(frm, text=board[i]).grid(column=0,row=i)
root.mainloop()