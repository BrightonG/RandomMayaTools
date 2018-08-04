#WIP
import pymel.core as pm

#Setup UVSets for storing Pivots
mesh = pm.ls(sl=True)[0].getShape()
while len(pm.polyUVSet(mesh, auv = True, query = True )) < 4:
    pm.polyUVSet(mesh, copy = True)
    
set = pm.polyUVSet(mesh, auv = True, query = True )
print set
setXY = set[2]
setZ = set[3]

pm.polyUVSet(mesh, rename = True, newUVSet='XY', uvSet= setXY)
pm.polyUVSet(mesh, rename = True, newUVSet='Z', uvSet= setZ)

pivot = pm.spaceLocator('PivotPoint')

#pm.polyListComponentConversion(pm.ls(sl=True), tuv=True)
#Select the UVS
selection = pm.ls(sl=True)
pm.polyUVSet(mesh, currentUVSet=True,  uvSet='XY')

pm.polyUVSet(mesh, cuv = True, uvSet = "Z" )
pm.select(pm.polyListComponentConversion(mesh, tuv=True))
ZLen = pm.polyEvaluate(mesh, uvs = "Z", uvc = True)
for i in xrange(ZLen):
    u, v = mesh.getUV(i, uvSet = "Z")
    mesh.setUV(i, u, 0, uvSet = "Z")
x,y,z = pivot.translate.get()
for vertex in selection:
    UVs = pm.polyListComponentConversion(vertex, tuv=True)
    for UV in UVs:
        a = UV.split('[')[1][:-1]
        idList = list(a.split(':'))
        for id in idList:
            mesh.setUV(id, x, y, uvSet = 'XY')
            mesh.setUV(id, z, 1, uvSet = 'Z')
    
    
