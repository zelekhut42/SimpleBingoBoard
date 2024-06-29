#functions and classes governing the creation of the bingo board

#imports
import tkinter as tk
import math
from functools import partial

#   object BingBoard
#   inherits tkinter Frame
#   creates and stores data for the bingo board

class BingoBoard(tk.Frame):

#       function __init__
#       initialization function for BingoBoard objects
#       inputs:
#           self: the object from which this function is being called, automaticaly filled
#           squares: organized list of text to be displayed on squares of the bingo board
#           master: the tkinter object that will contain the BingoBoard object
    
    def __init__(self, squares, master=None):
        tk.Frame.__init__(self, master)
        master.title("Raid Night Bingo")
        self.buttons = {}
        self.buttonStates = {}
        self.squareText = squares
        self.pack()
        self.CreateSquares()
        self.currentBingos = 0

#       function CreateSquares
#       function for creating, aligning, and defining the behaviour of the squares in the bingo board
#       inputs:
#           self: the object from which this function is being called, automaticaly filled

    def CreateSquares(self):
        xMax = math.sqrt(len(self.squareText))
        xPos = 0
        yPos = 0
        for square in self.squareText:
            if xPos == xMax:
                yPos += 1
                xPos = 0
            onClick = partial(self.Pressed, square) #function to be called when a bingo square is pressed
            button = tk.Button(self, text=str(square), fg="black", command=onClick, height=5, width=30)
            button.grid(row=yPos, column=xPos)
            self.buttons[str(square)] = button
            self.buttonStates[str(square)] = False
            xPos += 1

#       function Pressed
#       function for changing a binog square's color, state, and checking for bingo after it has been clicked on
#       inputs:
#           self: the object from which this function is being called, automaticaly filled
#           index: string of text on the bingo square that was clicked.

    def Pressed(self, index):
        #if the square is on turn it off
        if self.buttonStates[str(index)]:
            self.buttonStates[str(index)] = False
            self.buttons[str(index)].configure(bg="SystemButtonFace")
            self.CountBingos()  #update bingo state
        #if the square is off turn it on
        else:
            oldBingoCount = self.currentBingos
            self.buttonStates[str(index)] = True
            self.buttons[str(index)].configure(bg="red")
            self.CountBingos()  #update bingo state
            if self.currentBingos > oldBingoCount:
                print("new Bingo") #can be changed to do whatever you want when a bingo happens

#       function CountBingos
#       function for counting the current number of bingos on the bingo board and then updating the bingo board object with that information
#       inputs:
#           self: the object from which this function is being called, automaticaly filled

    def CountBingos(self):
        xMax = math.sqrt(len(self.squareText))
        yMax = xMax
        bingoCount = 0
        
        #count bingos in rows
        row = 1
        while row <= yMax:
            column = 1
            count = 0
            while column <= xMax:
                count += self.buttonStates[str(self.squareText[int(((row-1)*xMax+(column-1)))])] # adds true(1) or false(0) to the count
                column += 1
            if count == xMax:
                bingoCount += 1
            row += 1

        #count bingos in columns
        column = 1
        while column <= xMax:
            row = 1
            count = 0
            while row <= yMax:
                count += self.buttonStates[str(self.squareText[int(((row-1)*xMax+(column-1)))])] # adds true(1) or false(0) to the count
                row += 1
            if count == yMax:
                bingoCount += 1
            column += 1

        #top left to bottom right diagonal
        row = 1
        column = 1
        count = 0
        while row <= yMax:
            count += self.buttonStates[str(self.squareText[int(((row-1)*xMax+(column-1)))])] # adds true(1) or false(0) to the count
            column += 1
            row += 1
        if count == yMax:
                bingoCount += 1

        #bottom left to top right bingo
        row = 1
        column = xMax
        count = 0
        while row <= yMax:
            count += self.buttonStates[str(self.squareText[int(((row-1)*xMax+(column-1)))])] # adds true(1) or false(0) to the count
            column -= 1
            row += 1
        if count == yMax:
                bingoCount += 1

        #update how many bingos are there
        self.currentBingos = bingoCount
        
#   function CreateBingoBoard
#   function that creates and runs the bingo board
#   inputs:
#       squareText: organized list of text to be displayed on squares of the bingo board

def CreateBingoBoard(squareText):
    root = tk.Tk()
    app = BingoBoard(squareText, master=root)
    app.mainloop()

