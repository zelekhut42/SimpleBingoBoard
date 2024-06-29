#   functions that govern data procesing

#imports
import pandas as pd
import numpy as np
import math
import random

#   function ProcessData
#   function for reading a csv and returning a list of bingo squaress with a free space in the middle
#   inputs:
#       file: filename of the csv to be processed
#           CSV Notes: must contain a column titled "regular space", a column titled "free space", and my contain additional columns
#               regular space: contains the text for the squares for the bingo board, at a minimum must contain enough entries to populate all the squares of the bingo board or you will get an error
#               free space: contains the text for the free space square
#               additional column: title of column needs to be the exact same(case sensitive) as an entry in the regular space column, when that entry is selected it is replaced with a random entry from this column
#       size: size of the bingo board, note board is assumed to be a square with a side length of size
#   outputs:
#       Returns: the list of the text for the bingo board

def ProcessData(file, size):
    random.seed(a=None, version=2) #reset seed
    
    df = pd.read_csv(file, header=0) #read file into dataframe

    squareText = df[["regular space"]].sample(n=size*size-1).to_numpy().ravel().tolist() #randomly sample the regular spaces

    #process additional columns
    columnNames = df.columns.to_numpy().ravel().tolist()
    columnNames.remove("regular space")
    columnNames.remove("free space")
    position = -1
    for square in squareText:
        position += 1
        for column in columnNames:
            if square == column:
                squareText.pop(position)
                squareText.insert(position, df[[column]].dropna().sample(n=1).to_numpy().ravel().tolist()[0])

    #add free space
    freeSpaceText = df[["free space"]].dropna().sample(n=1).to_numpy().ravel().tolist()
    squareText.insert(size*math.floor(size/2)+math.ceil(size/2)-1, freeSpaceText[0])
    
    return squareText
