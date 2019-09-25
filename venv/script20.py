import rhinoscriptsyntax as rs
import random

pickedCurves = rs.GetObjects("pick some curves", 4)
pickedPoints = rs.GetObjects("pick some points", 1)

for curve in pickedCurves :
    distances = []
    for point in pickedPoints :
        thisDistance = rs.Distance(point, rs.CurveMidPoint(curve))
        distances.append(thisDistance)
    distancesAndPointsPaired = zip(distances, pickedPoints)
    #print distancesAndPointsPaired
    distancesAndPointsPaired.sort()
    closestPoint = distancesAndPointsPaired[0][1]
    rs.ExtrudeCurvePoint(curve, closestPoint)