import rhinoscriptsyntax as rs
import random

def blipCurve(y, bleepValue):

    x1 = random.uniform(0,10)
    z1 = random.uniform(0,10)
    x2 = random.uniform(10, 20)
    z2 = random.uniform(0, bleepValue)   #bleep
    x3 = random.uniform(20, 30)
    z3 = random.uniform(10, 20)
    x4 = random.uniform(30, 40)
    z4 = random.uniform(0, 10)
    x5 = random.uniform(40, 50)
    z5 = random.uniform(0, 10)

    listOfPoints = [(x1,y,z1), (x2,y,z2), (x3,y,z3), (x4,y,z4), (x5,y,z5)]
    return rs.AddInterpCurve(listOfPoints, 3)  ## 1: straight line, 2, 3,

for c in range(100):
    aCurve = blipCurve(c, 100)
    if c==68:
        rs.MoveObject(aCurve, (0,0,-100))