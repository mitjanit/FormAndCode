import rhinoscriptsyntax as rs
import random

count = 0
while count < 1000 :
    x = random.uniform(-10,10)
    y = random.uniform(-10,10)
    z = random.uniform(-10,10)
    point = (x, y, z)

    rs.AddPoint(point)

    count += 1