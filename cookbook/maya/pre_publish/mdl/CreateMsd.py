from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.core.msd as msd
import cgl.plugins.maya.alchemy_new as alc


class CreateMsd(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        writes out an msd file for the current scene
        """
        # we could use something like this if we actually want to use dependencies on these.
        # dependency_dict = {"mdl": [],
        #                    "anim": ['cam']}
        msd_obj = msd.MSD(path_object=alc.Scene().path_object, dcc="maya")
        msd_obj.write_msd()
        self.pass_check('Check Passed')
