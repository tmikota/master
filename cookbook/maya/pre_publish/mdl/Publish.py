from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya import alchemy as alc


class Publish(PreflightCheck):

    def getName(self):
        pass

    def run(self):

        alc.scene_object().publish()
        self.pass_check('Check Passed')
