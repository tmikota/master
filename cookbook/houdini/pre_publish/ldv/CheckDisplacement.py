from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc
import hou 

class CheckDisplacement(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        for mat in hou.node('/mat').children():
            for node in hou.node('/mat/{}'.format(mat)).children():
                if node.type().name() == 'redshift::Displacement':
                    disp_scale = node.parm('scale').eval()
                    if disp_scale > 1:
                        self.fail_check('Check Failed')

        self.pass_check('Check Passed')
