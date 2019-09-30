#Adds 1000 random points distant [90,95] from origin (0,0,0)

import rhinoscriptsyntax as rs
import random

count = 0
while count < 1000 :
    x = random.uniform(-100,100)
    y = random.uniform(-100,100)
    z = random.uniform(-100,100)
    point = (x, y, z)
    origin = (0,0,0)

    if rs.Distance(point, origin)>90 and rs.Distance(point, origin)<95 :
        rs.AddPoint(point)
        count += 1