import rhinoscriptsyntax as rs
import random

displaceX = 10;
displaceY = 10;

mirrorX = False

#start point
start   = (0,0,0)
end     = (0,100,0)

nCols = 6
nRows = 6
wSquare = 100

plane = rs.WorldXYPlane()
allRects = []
gridRects = []

# Add random rect from the grid
rs.AddLayer("Rects")
for r in range(0,nRows):
    for c in range(0, nCols):
        origin = (start[0] + wSquare*r, start[1] + wSquare*c, start[2])
        plane = rs.MovePlane(plane,origin)
        rn = random.uniform(0,10)
        if(rn<2):
            newRect = rs.AddRectangle(plane, wSquare, wSquare)
            rs.ObjectLayer(newRect, "Rects")
            gridRects.append(newRect)
            allRects.append(newRect)

# Rotate all rects from the grid
for rect in gridRects:
    for ntimes in range(1,4):
        newRect = rs.RotateObject( rect , start , 15.0*ntimes, None, True )
        rs.ObjectLayer(newRect, "Rects")
        allRects.append(newRect)

# Mirror all rects using Y axe
mirrorYRects = []
for rect in allRects:
    newRect = rs.MirrorObject( rect, start, end, True )
    mirrorYRects.append(newRect)

allRects.append(mirrorYRects);

# Mirror all rects using X axe
if(mirrorX):
    mirrorXRects = []
    for rect in allRects:
        newRect = rs.MirrorObject( rect, (-100,0,0), (100,0,0), True )
        mirrorXRects.append(newRect)

    allRects.append(mirrorXRects);

lines = []
rs.AddLayer("Split Lines")
for nl in range(1,16):
    coordA = (-800 + nl*100,-800,0)
    coordB = (-800 + nl*100, 800, 0)
    line = rs.AddLine(coordA, coordB);
    lines.append(line)
    rs.ObjectLayer(line, "Split Lines")

#for r in allRects:
 #   for l in lines:
 #       rs.SplitBrep ( r, l )
