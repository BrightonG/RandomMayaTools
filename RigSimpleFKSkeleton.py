import pymel.core as pm

def MakeControl(target, parent = None):
    pm.select(clear = True)
    
    #Make Object Names
    groupName = str(target) + "_Group"
    controlName = str(target) + "_Control"
    
    #Make Group Node
    grp = pm.group(name = groupName)
    pm.delete(pm.parentConstraint(target, grp))
    
    #Make Control Node
    cirTrans, cirShape = pm.circle(name = controlName, radius = 10)
    pm.parent(cirTrans, grp)
    pm.delete(pm.parentConstraint(target, cirTrans))
    pm.parentConstraint(cirTrans, target)
    return grp, cirTrans, target

selection = pm.ls(sl=True)

RigDict = {}
for item in selection:
    grp , control, bone = MakeControl(item)
    RigDict[str(item)] = {'control' : control, 'bone' : bone, 'group' : grp}
    
for key in RigDict:
    joint = RigDict[key]['bone']
    for relative in pm.listRelatives(joint, type = 'joint'):
        name = str(relative)
        for a in RigDict:
            if RigDict[a]['bone'] == name:
                pm.parent(RigDict[a]['group'],RigDict[key]['control'])
