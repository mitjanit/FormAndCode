import rhinoscriptsyntax as rs
import random
import math

z = -100
radius = 30
pi = math.pi

while z <=100 :
    theta = 0
    while theta < 2*pi :
        x = radius*math.cos(theta)
        y = radius*math.sin(theta)
        point = (x,y,z)
        rs.AddPoint(point)
        theta += .1
    z += .5