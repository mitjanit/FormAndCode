import rhinoscriptsyntax as rs
import random

for c in range(100):

    v1 = random.uniform(-100,100)
    v2 = random.uniform(-100,100)
    v3 = random.uniform(-100,100)
    pointA = [v1, v2, v3]

    v4 = random.uniform(-100, 100)
    v5 = random.uniform(-100, 100)
    v6 = random.uniform(-100, 100)
    pointB = [v4, v5, v6]

    v7 = random.uniform(-100, 100)
    v8 = random.uniform(-100, 100)
    v9 = random.uniform(-100, 100)
    pointC = [v7, v8, v9]

    rs.AddInterpCurve([pointA, pointB, pointC], 3)  ## 1: straight line, 2, 3, ...

