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

pickedSurface = rs.GetObjects("pick a surface", 8)

numUDivs = 20
numVDivs = 60

uDomain = rs.SurfaceDomain(pickedSurface, 0)
vDomain = rs.SurfaceDomain(pickedSurface, 1)

uMin = uDomain[0]
uMax = uDomain[1]
uRange = uMax - uMin
uStep = uRange / numUDivs

vMin = vDomain[0]
vMax = vDomain[1]
vRange = vMax - vMin
vStep = vRange / numVDivs

U = uMin
while U < uMax :
    V = vMin
    while V < vMax :
        normal = rs.SurfaceNormal(pickedSurface, (U,V))
        scaledNormal = rs.VectorScale(normal, 10)
        pointOnSurface = rs.EvaluateSurface(pickedSurface, U, V)
        pointOffSurface = rs.VectorAdd(pointOnSurface, scaledNormal)
        myTrunk = rs.AddLine(pointOnSurface, pointOffSurface)
        tree(myTrunk, 4, scaledNormal)
        V += vStep
    U += uStep