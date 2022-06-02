from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.maya import alchemy as alc
from cgl.plugins.maya import utils as utils
import getpass


class SetUpAovs(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """
        import pymel.core as pm
        aov_normals = pm.rsCreateAov(type='Normals')
        aov_beauty = pm.rsCreateAov(type='Beauty')

        aov_uv = pm.rsCreateAov(type='Custom')
        pm.setAttr('%s.name' % aov_uv, 'UV Checker', type='string')
        file_uv = pm.createNode('file')
        # path = 'C:\Users\getpass\PycharmProjects\cglumberjack\python\cglumberjack\resources\UDIM_Checker_Maps'
        path_1 = r'K:\global_library\asset\turntable\UDIM_Checker_Maps\UVChecker_1K.1001.png'
        pm.setAttr('%s.fileTextureName' % file_uv, path_1, type='string')
        pm.connectAttr('%s.outColor' % file_uv, '%s.defaultShader' % aov_uv, f=True)

        aov_udim = pm.rsCreateAov(type='Custom')
        pm.setAttr('%s.name' % aov_udim, 'UDIM', type='string')
        file_udim = pm.createNode('file')
        # path = 'C:\Users\getpass\PycharmProjects\cglumberjack\python\cglumberjack\resources\UDIM_Checker_Maps'
        path_2 = r'K:\global_library\asset\turntable\UDIM_Checker_Maps\UVChecker_1K.1002.png'
        pm.setAttr('%s.fileTextureName' % file_udim, path_2, type='string')
        pm.connectAttr('%s.outColor' % file_udim, '%s.defaultShader' % aov_udim, f=True)
        pm.setAttr('%s.uvTilingMode' % file_udim, 3)

        # aov = pm.rsCreateAov(type='Custom')
        # pm.setAttr('%s.name' % aov, 'UDIM', type='string')
        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
