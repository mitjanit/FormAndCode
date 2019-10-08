import rhinoscriptsyntax as rs
import random

displaceX = 10;
displaceY = 10;

#start point
start = (0,0,0)

wRect = 600;
hRect= 30;
gapY = 5;

numRects = 10
numCols = 5;
plane = rs.WorldXYPlane()
for i in range(0,numRects):
    origin = (start[0], start[1]+(gapY+hRect)*i, start[2])
    plane = rs.MovePlane(plane,origin)
    rs.AddRectangle(plane, wRect, hRect)
    newX = start[0]
    while newX < start[0]+wRect:
        dispX = random.uniform(3,10)
        newX = newX + dispX
        if(newX<start[0]+wRect):
            colA = (newX, start[1]+(gapY+hRect)*i, start[2])
            colB = (newX, start[1]+(gapY+hRect)*i + hRect, start[2])
            rs.AddLine(colA, colB)