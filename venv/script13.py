import rhinoscriptsyntax as rs
import random

def randCurve(numPoints):
    listOfPoints = []
    for q in range(numPoints):
        v1 = q
        v2 = random.triangular(-100,100,50)
        v3 = 0
        point = [v1, v2, v3]
        listOfPoints.append(point)

    rs.AddInterpCurve(listOfPoints, 3)  ## 1: straight line, 2, 3,

randCurve(100)