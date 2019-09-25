import rhinoscriptsyntax as rs
import random

pickedCurves = rs.GetObjects("pick some curves", 4)

if len(pickedCurves) < 2 :
    print("you must pick at least 2 curves")
else :
    random.shuffle(pickedCurves)
    rs.AddLoftSrf(pickedCurves)

#random.shuffle(pickedCurves)
#rs.AddLoftSrf(pickedCurves)
