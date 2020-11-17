import glob
from init import init
init()
import cells

print("Entering main loop...")
while(True):
    cells.cycle()
input()
