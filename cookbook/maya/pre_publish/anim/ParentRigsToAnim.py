from cgl.plugins.preflight.preflight_check import PreflightCheck

import maya.cmds as cmds


class ParentRigsToAnim(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        if not cmds.ls('ANIM'):
            cmds.group(em=True,name ='ANIM')
        
        rigs = cmds.ls('*:rig')
        for rig in rigs: 
            try: 
                cmds.parent(rig,'ANIM')
            except RuntimeError:
                pass

        print('PreflightTemplate')
        self.pass_check('Check Passed')
