import rhinoscriptsyntax as rs
import random
import math

z = -100
radius = 40
pi = math.pi

while z <=100 :
    theta = 0
    while theta < 2*pi :
        randomShift = random.uniform(-1,1)*(z/25.0)
        x = radius*math.cos(theta) + randomShift
        y = radius*math.sin(theta) + randomShift
        point = (x,y,z)
        rs.AddPoint(point)
        theta += .05 #random.uniform(-1.0,1.0)*z
    z += .3