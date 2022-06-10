from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc

class SetRenderSettings(PreflightCheck):

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
        out_root = hou.node('/out')

        if not out_root.children():
            redshift_node = out_root.createNode('Redshift_ROP')

        print('PreflightTemplate')
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
