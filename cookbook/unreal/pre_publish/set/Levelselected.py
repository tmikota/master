from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.unreal import alchemy as alc
import unreal


class Levelselected(PreflightCheck):

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
        selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
        if len(selected_assets) > 0:
            if selected_assets[0].get_class().get_name() == "World":
                self.pass_check('Check Passed')
            else:
                self.fail_check("Error: Selected Asset Must Be Level")
        else:
            self.fail_check("Error: No Asset Selected")
