# Projection of curves on a surface
# Use different layers to display different line stroke width.


import rhinoscriptsynatx as rs

curves = rs.ObjectsByType(4);
picturePlane = rs.GetObject("Pick the picture plane", 8)
eyePoint = rs.getObject("Pick the eye point", 1);

for curve in curves:
    pointsOnCurve = rs.DivideCurve(curve, 100)
    intersectionPoints = []
    for point in pointsOnCurve :
        d = rs.Distance(point, eyePoint)
        if d<1000:
            layerName = "close"
        elif d>=1000 and d<1300:
            layerName = "middle"
        else :
            layerName = "far"
        projector = rs.AddLine(point, eyePoint)
        rs.ObjectLayer(projector, layerName)
        intersections = rs.CurveSurfaceIntersection(projector, picturePlane)
        if intersections :
            intersectionPoint = intersections[0][1]
            intersectionPoints.append(intersectionPoint)
        pointObs = rs.AddPoints(intersectionPoints)
        reconstructedCurve = rs.AddInterpCurve(intersectionPoints, 1)
        rs.ObjectLayer(reconstructedCurve, "drawingOnSurface")