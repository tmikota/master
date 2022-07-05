from cgl.plugins.preflight.preflight_check import PreflightCheck

import maya.cmds as cmds


class ParentRigsToAnim(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        if not cmds.ls('anim'):
            cmds.group(em=True,name ='anim')
        
        rigs = cmds.ls('*:rig')
        for rig in rigs: 
            try: 
                cmds.parent(rig,'anim')
            except RuntimeError:
                pass

        print('PreflightTemplate')
        self.pass_check('Check Passed')
