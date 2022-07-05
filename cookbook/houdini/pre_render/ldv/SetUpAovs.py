from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


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
        import hou
        rs = hou.node('/out/Redshift_ROP1')
        rs.parm('RS_aov').set(4)
        rs.parm('RS_aovID_1').set(24)
        rs.parm('RS_aovSuffix_1').set('Normals')

        rs.parm('RS_aovID_2').set(39)
        rs.parm('RS_aovSuffix_2').set('Beauty')

        rs.parm('RS_aovID_3').set(8)
        rs.parm('RS_aovSuffix_3').set('specular')

        rs.parm('RS_aovID_4').set(25)
        rs.parm('RS_aovSuffix_4').set('bN')

        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
