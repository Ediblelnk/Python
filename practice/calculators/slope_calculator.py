run = True
while run:

    def getslope(x1,y1,x2,y2):
        slope = (y1-y2)/(x1-x2)
        print(slope)
    
    point1 = input("Point 1?\t").split(sep=", ")
    point2 = input("Point 2?\t").split(sep=", ")
    x1 = float(point1[0])
    y1 = float(point1[1])
    x2 = float(point2[0])
    y2 = float(point2[1])
    getslope(x1,y1,x2,y2)
