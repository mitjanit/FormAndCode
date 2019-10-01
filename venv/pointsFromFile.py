# Import points from a text file
# Based on https://developer.rhino3d.com/samples/rhinopython/import-points/

import rhinoscriptsyntax as rs

importedPoints = []

def ImportPoints():
    # prompt the user for a file to import
    filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    # read each line from the file
    file = open(filename, "r")
    contents = file.readlines()
    file.close()

    # local helper function
    def __point_from_string(text):
        items = text.strip("()\n").split(",")
        x = float(items[0])
        y = float(items[1])
        z = float(items[2])
        return x, y, z

    points = [__point_from_string(line) for line in contents]
    rs.AddPoints(points)
    return points


##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if (__name__ == "__main__"):
    importedPoints = ImportPoints()
    print(importedPoints)