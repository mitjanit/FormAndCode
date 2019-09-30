# recursion tree

import rhinoscruptsyntax as rs
import random

def tree(trunk, desiredLevel, currentLevel=0):
    endPoint = rs.CurveEndPoint(trunk)
    newPoint1 = (endPoint[0]+random.uniform(-5,5), endPoint[1]+random.uniform(-5,5), endPoint[2]+random.uniform(0,5))
    newPoint2 = (endPoint[0]+random.uniform(-5,5), endPoint[1]+random.uniform(-5,5), endPoint[2]+random.uniform(0,5))
    newBranch1 = rs.AddLine(endPoint, newPoint1)
    newBranch2 = rs.AddLine(endPoint, newPoint2)

    if currentLevel<desiredLevel :
        tree(newBranch1, desiredLevel, currentLevel+1)
        tree(newBranch2, desiredLevel, currentLevel+1)

startLine = rs.AddLine((0,0,0),(0,0,20))
tree(startLine, 3)