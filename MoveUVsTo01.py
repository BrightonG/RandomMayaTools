import pymel.core as pm
import math

selection = pm.ls(sl=True)
for item in selection:    
    shape = pm.PyNode(item.node())
    UVCount = len(shape.getUVs()[0])
    xRegion = 0
    yRegion = 0    
    for i in xrange(0, UVCount):
        x, y = shape.getUV(i)
        xRegion = x + xRegion
        yRegion = y + yRegion
    if(yRegion < 0):
        yTemp = yRegion
    else:
        yTemp = yRegion
    if(xRegion < 0):
        xTemp = xRegion
    else:
        xTemp = xRegion
    frac, xOffset = math.modf(xTemp / UVCount)
    frac, yOffset = math.modf(yTemp / UVCount) 
    if(yRegion < 0):
        yOffset = yOffset + -1
    if(xRegion < 0):
        xOffset = xOffset + -1
    for i in xrange(0, UVCount):
        x, y = shape.getUV(i)
        newX = x - xOffset
        newY = y - yOffset
        shape.setUV(i,newX,newY)
