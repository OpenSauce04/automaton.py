from random import choice
import glob
import find
import move
from copy import copy, deepcopy

global cellsnew
global newcellarray
global nextid
nextid=0
def newcell():
    global nextid
    nextid+=1
    return [nextid,40,-1,-1]
newcellarray=[[[0 for x in range(4)] for y in range(glob.worldSize)] for z in range(glob.worldSize)]
cells=new_array = list(map(list, newcellarray))
cells[int(glob.worldSize/2)][int(glob.worldSize/2)]=newcell()

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
    global newcellarray
    glob.cycleno+=1
    print("\nCycle "+str(glob.cycleno)+": ")
    glob.cellno=0
    cellsnew = list(map(list, newcellarray))
    for h in range(glob.worldSize):
        for w in range(glob.worldSize):
            if (cells[w][h][0]!=0):
                glob.cellno+=1
                if (glob.world[w][h] == 'f'):
                    print("C"+str(cells[w][h][0])+": Reached food")
                    cells[w][h][2] = -1
                    glob.world[w][h]='g'
                    cells[w][h][1]+=20
                    for x in range(1): # I know this code is weird but I couldn't think of a better way to do it
                        if (cells[w][h][1]>100): # If enough food to create offspring
                            if (cells[w][h+1][0]==0): cells[w][h][1]-=50; cells[w][h+1]=newcell()
                            elif (cells[w][h-1][0]==0): cells[w][h][1]-=50; cells[w][h-1]=newcell()
                            elif (cells[w+1][h][0]==0): cells[w][h][1]-=50; cells[w+1][h]=newcell()
                            elif (cells[w-1][h][0]==0): cells[w][h][1]-=50; cells[w-1][h]=newcell()
                            elif (cells[w+1][h+1][0]==0): cells[w][h][1]-=50; cells[w+1][h+1]=newcell()
                            elif (cells[w+1][h-1][0]==0): cells[w][h][1]-=50; cells[w+1][h-1]=newcell()
                            elif (cells[w+1][h-1][0]==0): cells[w][h][1]-=50; cells[w+1][h-1]=newcell()
                            elif (cells[w-1][h-1][0]==0): cells[w][h][1]-=50; cells[w-1][h-1]=newcell()
                            else: break
                        print("C"+str(nextid)+" was born.")
                if(cells[w][h][2]==-1):
                    try:
                        foodlocation=find.nearestFood(w,h)
                        print("C"+str(cells[w][h][0])+": Found food at "+str(foodlocation)+", Travelling...")
                        cells[w][h][2]=foodlocation[0]
                        cells[w][h][3]=foodlocation[1]
                    except:
                        cells[w][h][2]=-1
                if(cells[w][h][2]==-1): # No food in vacinity, move randomly
                    moveswitch = {
                        'u': ucase,
                        'd': dcase,
                        'l': lcase,
                        'r': rcase
                    }
                    movefunction=choice(list(moveswitch.values()))
                    movefunction(w,h)
                else: # Knows food whereabouts, move towards
                    newcoords=move.moveTowards(w,h,cells[w][h][2],cells[w][h][3])
                    nw=newcoords[0]
                    nh=newcoords[1]
                    if cells[nw][nh][0]!=0:
                        cellsnew[w][h]=cells[w][h]
                    else:
                        cellsnew[nw][nh]=cells[w][h]
                print("C"+str(cells[w][h][0])+": Moved to "+str(w)+", "+str(h)+"; Now has "+str(cells[w][h][1])+" food")
                cells[w][h][1]-=1
                if cells[w][h][1]<=0:
                    print("C"+str(cells[w][h][0])+": Starved to death")
                    glob.deathcount+=1
                    cellsnew[w][h]=[0,0]
    print('-'*17)
    print("Cell count:  "+str(glob.cellno))
    print("Death count: "+str(glob.deathcount))
    cells=cellsnew
    if (glob.cellno==0):
        print("All cells died")
        input()
        exit()
