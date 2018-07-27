import pymel.core as pm
import math

selection = pm.ls(sl=True)
for item in selection:    
    #Get Shape Node from selected Transform
    shape = pm.PyNode(item.node())
    #Get the UV Length
    UVCount = len(shape.getUVs()[0])
    xRegion = 0
    yRegion = 0
    #Calculate the UDIM Section by via Sum & Divide
    for i in xrange(0, UVCount):
        x, y = shape.getUV(i)
        xRegion = x + xRegion
        yRegion = y + yRegion
    #Handle Negative UDIM sections
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
    # Move each UV by the UDIM offset so that every UV is in 0-1 space.
    for i in xrange(0, UVCount):
        x, y = shape.getUV(i)
        newX = x - xOffset
        newY = y - yOffset
        shape.setUV(i,newX,newY)
