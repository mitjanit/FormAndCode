import rhinoscriptsyntax as rs
import random

def randCurve(numPoints):
    listOfPoints = []
    for q in range(numPoints):
        v1 = random.uniform(-100,100)
        v2 = random.uniform(-100,100)
        v3 = random.uniform(-100,100)
        point = [v1, v2, v3]
        listOfPoints.append(point)

    rs.AddInterpCurve(listOfPoints, 3)  ## 1: straight line, 2, 3, ...

for c in range(10):
    randCurve(c+2)