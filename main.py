#   This program is a simple bingo board origionaly created for personal use.
#   It reads a specialy created CSV file in order to get the text for the bino board squares.
#   If a bingo(all of one row, column, or diagonal is fully filled) is reached this program will print out that a new bingo has occured.
#   This behavior can be changed in bingo_board.py.
#   The specialy created CSV must contain a column titled "regular space", a column titled "free space", and my contain additional columns.
#   The regular space column contains the text for the squares for the bingo board, and at a minimum must contain enough entries to populate all the squares of the bingo board or you will get an error.
#   The free space column contains the text for the free space square.
#   Any additional columns need a title that is the exact same(case sensitive) as an entry in the recular space column, and when that entry is selected to be in the bingo board it is replaced with a random entry from this column

#imports
import data_processing
import bingo_board

#global variables
size = 5   #length on one side of the bingo board, bingo boards are squares
file = "Example.csv"  #file name of the file to be used

squareText = data_processing.ProcessData(file, size)

bingo_board.CreateBingoBoard(squareText)
