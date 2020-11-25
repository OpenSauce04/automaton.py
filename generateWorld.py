import glob
from math import floor
from random import randint
import sys

def generateTile():
    if (floor(randint(0,10))==0):
        return 'f'
    return 'g'
def generateWorld():
    glob.world=[['g']*glob.worldSize for i in range(glob.worldSize)]
    counter=0
    ppercentage=''
    for h in range(glob.worldSize):
        for w in range(glob.worldSize):
            glob.world[w][h]=generateTile()
            counter+=1
        percentage=floor(100*counter/glob.worldSize**2)
        if (percentage!=ppercentage):
            print(str(percentage) + "%")
        ppercentage=percentage