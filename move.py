def moveTowards(x,y,tx,ty):
    rx=x
    ry=y
    if (x<tx): rx+=1
    elif (x>tx): rx-=1
    elif (y<ty): ry+=1
    elif (y>ty): ry-=1
    return [rx,ry]