# Projection of curves on a surface
# Use different layers (process and drawingOnSurface) for process and final drawing.


import rhinoscriptsynatx as rs

curves = rs.ObjectsByType(4);
picturePlane = rs.GetObject("Pick the picture plane", 8)
eyePoint = rs.getObject("Pick the eye point", 1);

for curve in curves:
    pointsOnCurve = rs.DivideCurve(curve, 100)
    intersectionPoints = []
    for point in pointsOnCurve :
        projector = rs.AddLine(point, eyePoint)
        rs.ObjectLayer(projector, "process")
        intersections = rs.CurveSurfaceIntersection(projector, picturePlane)
        if intersections :
            intersectionPoint = intersections[0][1]
            intersectionPoints.append(intersectionPoint)
        pointObs = rs.AddPoints(intersectionPoints)
        reconstructedCurve = rs.AddInterpCurve(intersectionPoints, 1)
        rs.ObjectLayer(reconstructedCurve, "drawingOnSurface")
