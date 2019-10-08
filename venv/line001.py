import rhinoscriptsyntax as rs

displaceX = 10;
displaceY = 10;

#start point
start = (0,0,0)

widthGrid = 100;
heightGrid = 100;

numRows = 11
numCols = 11
for i in range(0,numRows):
    newY = start[1] + displaceY*i
    coordA = (start[0], newY, start[2])
    coordB = (start[0]+widthGrid, newY, start[2])
    rs.AddLine(coordA, coordB)
    if(i<numRows-1):
        for j in range(0,numCols):
            newX = start[0] + displaceX*j
            coordC = (newX, newY, start[2])
            coordD = (newX, newY + displaceY, start[2])
            print(coordC, coordD)
            rs.AddLine(coordC, coordD)


#plane = rs.WorldXYPlane()
#rs.AddRectangle(plane, widthGrid, heightGrid)