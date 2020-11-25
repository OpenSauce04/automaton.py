import glob
from generateWorld import generateWorld
def init():
    print("Initializing variables...")
    glob.worldSize = 1000
    glob.cycleno = 0
    glob.cellno = 0
    glob.deathcount = 0
    print(" Generating World ")
    glob.cells = generateWorld()
