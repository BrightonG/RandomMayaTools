import pymel.core as pm
Begin = -1
End = 14
COUPLES = list()
bones = pm.ls(type='joint')

class JointCouple():
    def __init__(self, Joint):
        self.Joint = Joint
        locName = 'loc_' + str(Joint)
        self.Loc = pm.spaceLocator(name = locName)
        origName = str(Joint)+'_orig'
        self.Original = pm.spaceLocator(name=origName)
    
    def ConstrainLoc2Joint(self):
        self.Constraint = pm.parentConstraint(self.Joint, self.Loc)
    
    def ConstrainJoint2Loc(self):
        self.Constraint = pm.parentConstraint(self.Loc, self.Joint)
    
    def DeleteConstraint(self):
        if self.Constraint:
            pm.delete(self.Constraint)
        else:
            print "There is no constraint to delete"
    
    def ConstrainOriginalAnimation(self):
        self.OriginalConstraint = pm.parentConstraint(self.Joint, self.Original)
    
    def DeleteConstraintFromOriginal(self):
        pm.delete(self.OriginalConstraint)

    def ConstrainLoc2Original(self):
        self.Constraint = pm.parentConstraint(self.Original, self.Loc)

    def ClearJointAnimation(self):
        pm.cutKey(self.Joint)

def makeCouples():
    for bone in bones:
        localCouple = JointCouple(bone)
        COUPLES.append(localCouple)

def StoreAnimation():
    for item in COUPLES:
        item.ConstrainOriginalAnimation()
    Originals = [o.Original for o in COUPLES]
    pm.bakeResults( Originals , t=(Begin, End), simulation=True )
    for item in COUPLES:
        item.DeleteConstraintFromOriginal()

def TransferAnimation():
    for item in COUPLES:
        item.ConstrainLoc2Joint()
    locators = [o.Loc for o in COUPLES]
    pm.bakeResults( locators , t=(Begin, End), simulation=True )
    for item in COUPLES:
        item.DeleteConstraint()
        item.ConstrainJoint2Loc()
        item.ClearJointAnimation()

print "Making Couples"
makeCouples()
print "Storing Original Animation"
StoreAnimation()
print "Transfering Animation to Locators"
TransferAnimation()