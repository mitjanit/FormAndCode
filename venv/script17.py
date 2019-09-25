import rhinoscriptsyntax as rs
import random

pickedCurves = rs.GetObjects("pick some curves", 4)
desiredArea = 300.0

for curve in pickedCurves:
    length = rs.CurveLength(curve)
    extrudeAmt = desiredArea / length
    directionalVector = (random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))
    unitVector = rs.VectorUnitize(directionalVector)
    scaledVector = rs.VectorScale(unitVector, extrudeAmt)
    startPoint = rs.CurveMidPoint(curve)
    endPoint = rs.VectorAdd(startPoint, scaledVector)
    pathCurve = rs.AddLine(startPoint, endPoint)
    rs.ExtrudeCurve(curve, pathCurve)
    rs.DeleteObject(pathCurve)