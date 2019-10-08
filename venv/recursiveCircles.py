import rhinoscriptsyntax as rs


def RecursiveCircle(pt, r):
    if r == 0:
        return 1
    else:
        rs.AddCircle(pt, r)
        return RecursiveCircle(pt, r - 1)


pt = rs.GetPoint("Pick starting point")

RecursiveCircle(pt, 10)