from random import choice
import glob
global nextid
global cellsnew
global nextid
nextid=0
def newcell():
    global nextid
    nextid+=1
    return [nextid,40]
cells=[[[0 for x in range(2)] for y in range(glob.worldSize)] for z in range(glob.worldSize)]
cells[int(glob.worldSize/2)][int(glob.worldSize/2)]=newcell()
nextid+=1

def ucase(w,h):
    if cells[w][h+1][0]!=0:
        cellsnew[w][h]=cells[w][h]
        return
    cellsnew[w][h+1]=cells[w][h]
def dcase(w,h):
    if cells[w][h-1]!=0:
        cellsnew[w][h]=cells[w][h]
        return
    cellsnew[w][h-1]=cells[w][h]
def lcase(w,h):
    if cells[w-1][h][0]!=0:
        cellsnew[w][h]=cells[w][h]
        return
    cellsnew[w-1][h]=cells[w][h]
def rcase(w,h):
    if cells[w+1][h][0]!=0:
        cellsnew[w][h]=cells[w][h]
        return
    cellsnew[w+1][h]=cells[w][h]
def cycle():
    global cellsnew
    global cells
    glob.cycleno+=1
    print("\nCycle "+str(glob.cycleno)+": ")
    glob.cellno=0
    cellsnew=[[[0]*2]*glob.worldSize for i in range(glob.worldSize)]
    for h in range(glob.worldSize):
        for w in range(glob.worldSize):
            if (cells[w][h][0]!=0):
                glob.cellno+=1
                moveswitch = {
                    'u': ucase,
                    'd': dcase,
                    'l': lcase,
                    'r': rcase
                }
                movefunction=choice(list(moveswitch.values()))
                movefunction(w,h)
                print("C"+str(cells[w][h][0])+": Moved to "+str(w)+", "+str(h)+"; Now has "+str(cells[w][h][1])+" food")
                if (glob.world[w][h]=='f'):
                    print("C"+str(cells[w][h][0])+": Found food")
                    glob.world[w][h]='g'
                    cells[w][h][1]+=20
                    if (cells[w][h][1]>100):
                        cells[w][h][1]-=50
                cells[w][h][1]-=1
                if cells[w][h][1]<=0:
                    print("C"+str(cells[w][h][0])+": Died")
                    newcells[w][h]=[0,0]
    cells=cellsnew
    if (glob.cellno==0):
        print("All cells died")
        input()
        exit()