#Adds 1000 random points inside a boolean space

import rhinoscriptsyntax as rs
import random

count = 0
while count < 9000 :
    x = random.uniform(-100,100)
    y = random.uniform(-100,100)
    z = random.uniform(-100,100)
    point = (x, y, z)

    if (x>-20 and x<95 and y>-75 and y<50 and z>-50 and z<90) and not(x>-30 and x<65 and y>-95 and y<40 and z>-10 and z<20) :
        rs.AddPoint(point)
        count += 1
