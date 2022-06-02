from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc


class Publish(PreflightCheck):

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
		publish_render_object = alc.scene_object().publish()
		if(os.path.isfile(publish_render_object.path_root)):
			self.pass_check('Cloth rig published, success')
		else:
			self.fail_check('Cloth rig publish, fail')
