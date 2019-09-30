#Add points along a cone surface

import rhinoscriptsyntax as rs
import random
import math

z = -100
radius = 0
theta = 0

while z <=100 :
    x = radius*math.cos(theta)
    y = radius*math.sin(theta)
    point = (x,y,z)
    rs.AddPoint(point)
    radius += .003
    theta += 1
    z += .01