

import rhinoscriptsynatx as rs

points = rs.GetObjects("pick some points to map", 8)
referenceSurface = rs.GetObject("pick the reference surface", 8)
destinationSurface = rs.GetObject("pick the destination surface", 8)
listOfDestinationPoints = []

for point in points :
    UV = rs.SurfaceClosestPoint(referenceSurface, point)
    U = UV[0]
    V = UV[1]
    domainUReference = rs.SurfaceDomain(referenceSurface, 0)
    domainVReference = rs.SurfaceDomain(referenceSurface, 1)
    rangeUReference = domainUReference[1] - domainUReference[0]
    rangeVRefrence = domainVReference[1] - domainVReference[0]
    relativeU = (U - domainUReference[0])/rangeUReference
    relativeV = (V - domainVReference[0])/rangeVRefrence

    domainUDestination = rs.SurfaceDomain(destinationSurface, 0)
    domainVDestination = rs.SurfaceDomain(destinationSurface, 1)
    rangeUDestination = domainUDestination[1] - domainUDestination[0]
    rangeVDestination = domainVDestination[1] - domainVDestination[0]
    absoluteU = relativeU*rangeUDestination + domainUDestination[0]
    absoluteV = relativeV*rangeVDestination + domainVDestination[0]

    pointOnDestination = rs.EvaluateSurface(destinationSurface, absoluteU, absoluteV)
    listOfDestinationPoints.append(pointOnDestination)
    rs.AddPoint(pointOnDestination)