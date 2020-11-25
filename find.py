import glob
def nearestFood(w,h):
    food=[]
    for layerNumber in range(1,10):
        if (glob.world[w - layerNumber][h + layerNumber]=='f'): food.append([w - layerNumber, h + layerNumber])
        if (glob.world[w - layerNumber][h - layerNumber]=='f'): food.append([w - layerNumber, h - layerNumber])
        if (glob.world[w + layerNumber][h + layerNumber]=='f'): food.append([w + layerNumber, h + layerNumber])
        if (glob.world[w + layerNumber][h - layerNumber]=='f'): food.append([w + layerNumber, h - layerNumber])
        for decValue in range(layerNumber):
            if (glob.world[w - layerNumber][h + decValue]=='f'): food.append([w - layerNumber, h + decValue])
            if (glob.world[w + decValue][h + layerNumber]=='f'): food.append([w + decValue, h + layerNumber])
            if (glob.world[w + decValue][h - layerNumber]=='f'): food.append([w + decValue, h - layerNumber])
            if (glob.world[w + layerNumber][h + decValue]=='f'): food.append([w + layerNumber, h + decValue])
            if (decValue != 0):
                if (glob.world[w - layerNumber][h - decValue]=='f'): food.append([w - layerNumber, h - decValue])
                if (glob.world[w + layerNumber][h - decValue]=='f'): food.append([w + layerNumber, h - decValue])
                if (glob.world[w - decValue][h + layerNumber]=='f'): food.append([w - decValue, h + layerNumber])
                if (glob.world[w - decValue][h - layerNumber]=='f'): food.append([w - decValue, h - layerNumber])
        if (len(food)>0):
            return(food[0])
            break