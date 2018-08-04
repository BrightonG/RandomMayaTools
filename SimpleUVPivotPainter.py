import pymel.core as pm

#Setup UVSets for storing Pivots
mesh = pm.ls(sl=True)[0].getShape()
while len(pm.polyUVSet(mesh, auv = True, query = True )) < 4:
    #Pivots are encoding into UV2 UV3
    pm.polyUVSet(mesh, copy = True)
    
set = pm.polyUVSet(mesh, auv = True, query = True )
setXY = set[2]
setZ = set[3]

pm.polyUVSet(mesh, rename = True, newUVSet='XY', uvSet= setXY)
pm.polyUVSet(mesh, rename = True, newUVSet='Z', uvSet= setZ)

selection = pm.ls(sl=True)

pivot = pm.spaceLocator('PivotPoint')

#Clear out existing XY.Z UVs
pm.polyUVSet(mesh, cuv = True, uvSet = setZ )
pm.select(pm.polyListComponentConversion(mesh, tuv=True))
ZLen = pm.polyEvaluate(mesh, uvs = setZ, uvc = True)
for i in xrange(ZLen):
    mesh.setUV(i, 0, 0, uvSet = setZ)

pm.polyUVSet(mesh, cuv = True, uvSet = setXY )
pm.select(pm.polyListComponentConversion(mesh, tuv=True))
XYLen = pm.polyEvaluate(mesh, uvs = setXY, uvc = True)
for i in xrange(XYLen):
    mesh.setUV(i, 0, 0, uvSet = setXY)

# Set UVs to world spaec coordinates of the locator
x,y,z = pivot.translate.get()
for vertex in selection:
    UVs = pm.polyListComponentConversion(vertex, tuv=True)
    for UV in UVs:
        a = UV.split('[')[1][:-1]
        idList = list(a.split(':'))
        for id in idList:
            mesh.setUV(id, x, y, uvSet = setXY)
            mesh.setUV(id, z, 1, uvSet = setZ)
    
    
