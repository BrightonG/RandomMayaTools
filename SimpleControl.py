import pymel.core as pm

def MakeControl(constrainTarget = False):
    for target in pm.ls(sl= True):
        #Selected object is the target
        pm.select(clear = True)
        
        #Make Object Names
        groupName = str(target[0]) + "_Group"
        controlName = str(target[0]) + "_Control"
        
        #Make Group Node
        grp = pm.group(name = groupName)
        con = pm.parentConstraint(target, grp)
        pm.delete(con)
        
        #Make Control Node
        cirTrans, cirShape = pm.circle(name = controlName, radius = 10)
        pm.parent(cirTrans, grp)
        con = pm.parentConstraint(target, cirTrans)
        pm.delete(con)
        
        #Constrain target
        if constrainTarget:
            pm.parentConstraint(cirTrans, target)

MakeControl(True)
