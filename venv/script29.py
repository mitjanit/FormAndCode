# Projection of curves on a surface
# Use different layers to display different line stroke width.


import rhinoscriptsynatx as rs

curves = rs.ObjectsByType(4);
picturePlane = rs.GetObject("Pick the picture plane", 8)
eyePoint = rs.getObject("Pick the eye point", 1);

for curve in curves:
    pointsOnCurve = rs.DivideCurve(curve, 100)
    intersectionPoints = []
    closeCount = 0
    middleCount = 0
    farCount = 0
    for point in pointsOnCurve :
        d = rs.Distance(point, eyePoint)
        if d<1000:
            layerName = "close"
            closeCount += 1
        elif d>=1000 and d<1300:
            layerName = "middle"
            middleCount += 1
        else :
            layerName = "far"
            farCount += 1
        projector = rs.AddLine(point, eyePoint)
        rs.ObjectLayer(projector, layerName)
        pointObject = rs.AddPoint(point)
        rs.ObjectLayer(pointObject, layerName)
        intersections = rs.CurveSurfaceIntersection(projector, picturePlane)
        if intersections :
            intersectionPoint = intersections[0][1]
            intersectionPoints.append(intersectionPoint)
        pointObs = rs.AddPoints(intersectionPoints)
        reconstructedCurve = rs.AddInterpCurve(intersectionPoints, 1)

        if closeCount>middleCount and closeCount>farCount :
            rs.ObjectLayer(reconstructedCurve, "close")
        elif middleCount > farCount :
            rs.ObjectLayer(reconstructedCurve,"middle")
        else :
            rs.ObjectLayer(reconstructedCurve, "far")