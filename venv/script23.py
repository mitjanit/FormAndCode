import rhinoscriptsyntax as rs
import random

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
        rs.AddLine(pointOnSurface, pointOffSurface)
        V += vStep
    U += uStep