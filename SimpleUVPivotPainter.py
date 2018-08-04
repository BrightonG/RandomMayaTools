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

#derp = pm.polyListComponentConversion(tuv=True)
#print derp
#newsel = pm.ls(sl = True)
#for v in newsel:
#    for uv in pm.polyListComponentConversion(v, tuv=True):
#        print uv
    
# Set UVs to world spaec coordinates of the locator
x,y,z = pivot.translate.get()
pm.polyUVSet(mesh, cuv = True, uvSet = setXY )
mesh.setUV(70, .5, .6, uvSet = setXY)
for item in selection:
    print item
#TODO: Selection is not iterating: 'pCubeShape1.vtx[12:27]'
for vertex in selection:
    print vertex
    UVs = pm.polyListComponentConversion(vertex, tuv=True)
    for uv in UVs:
        a = uv.split('[')[1][:-1]
        if ":" in a:
            ids = a.split(':')
            for id in ids:
                for i in xrange(XYLen):
                    if i == int(id):
                        mesh.setUV(i, x, y, uvSet = setXY)
                        print 'Match'
                    else:
                        mesh.setUV(i, 0, 0, uvSet = setXY)
        else:
            mesh.setUV(a, x, y, uvSet = setXY)
            print "elsed"


pm.polyUVSet(mesh, cuv = True, uvSet = setZ )
for vertex in selection:
    UVCount = len(mesh.getUVs(setZ)[0])
    for UV in xrange(UVCount):
        mesh.setUV(UV, z, 1, uvSet = setZ)
