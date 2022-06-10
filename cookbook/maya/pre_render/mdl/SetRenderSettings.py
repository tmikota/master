from cgl.plugins.preflight.preflight_check import PreflightCheck


# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.maya import alchemy as alc


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
        import pymel.core as pm
        fail = False
        pm.setAttr("defaultRenderGlobals.currentRenderer", "redshift", type="string")
        pm.setAttr("defaultRenderGlobals.imageFilePrefix", "<RenderLayer>/<Scene>", type="string")
        pm.setAttr("redshiftOptions.imageFormat", 1)
        pm.setAttr("redshiftOptions.exrForceMultilayer", 1)
        all_cams = pm.ls(type='camera')
        if 'turntable_cameraShape1' in all_cams:
            for cam in all_cams:
                pm.setAttr(f"{cam}.renderable", False)
            pm.setAttr("turntable_cameraShape1.renderable", True)
        else:
            fail = True
            print('Error: Cannot find turntable_camera1 to assign as renderable')
            # pm.error('Cannot find turntable_camera1')

        if not fail:
            self.pass_check('Check Passed')
        else:
            self.fail_check('Check Failed. Check Script Editor for errors')
        print('PreflightTemplate')
