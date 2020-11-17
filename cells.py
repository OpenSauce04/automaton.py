from random import choice
import glob
cells=[[False]*glob.worldSize for i in range(glob.worldSize)]
cells[round(glob.worldSize/2)][round(glob.worldSize/2)]=True
def ucase(w,h):
    if cells[w][h+1]:
        return
    cellsnew[w][h+1]=1
def dcase(w,h):
    if cells[w][h-1]:
        return
    cellsnew[w][h-1]=1
def lcase(w,h):
    if cells[w-1][h]:
        return
    cellsnew[w-1][h]=1
def rcase(w,h):
    if cells[w+1][h]:
        return
    cellsnew[w+1][h]=1
def cycle():
    global cellsnew
    global cells
    glob.cycleno+=1
    print("Cycle "+str(glob.cycleno)+": ")
    glob.cellno=0
    cellsnew=[[False]*glob.worldSize for i in range(glob.worldSize)]
    for h in range(glob.worldSize):
        for w in range(glob.worldSize):
            if cells[w][h]:
                print("cell at "+str(w)+", "+str(h))
                glob.cellno+=1
                moveswitch = {
                    'u': ucase,
                    'd': dcase,
                    'l': lcase,
                    'r': rcase
                }
                movefunction=choice(list(moveswitch.values()))
                movefunction(w,h)
    cells=cellsnew