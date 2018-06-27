import pymel.core as pm

def MakeControl(constrainTarget = False):
    selection = pm.ls(sl= True)
    for target in selection:
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
        #cmds.delete(cmds.parentConstraint(B, A))
        
        #Constrain target
        if constrainTarget:
            pm.parentConstraint(cirTrans, target)

def MakeBonesFromSelection(suffix = "_joint"):
        selection = pm.ls(sl= True)
        for target in selection:
            pm.select(clear = True)
            jointName = str(target) + suffix
            jnt = pm.joint(name = jointName)
            con = pm.parentConstraint(target, jnt)
            pm.delete(con)
#MakeControl(True)
#MakeBonesFromSelection()
