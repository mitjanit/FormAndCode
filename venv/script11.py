import rhinoscriptsyntax as rs
import random

numCurves = 10
numPoints = 5
for c in range(numCurves):
    listOfPoints = []
    for q in range(numPoints):
        v1 = random.uniform(-100,100)
        v2 = random.uniform(-100,100)
        v3 = random.uniform(-100,100)
        point = [v1, v2, v3]
        listOfPoints.append(point)

    rs.AddInterpCurve(listOfPoints, 3)  ## 1: straight line, 2, 3, ...

