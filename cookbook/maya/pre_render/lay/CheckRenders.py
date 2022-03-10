from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.maya.alchemy as alc
from cgl.ui.widgets.dialog import InputDialog
import os


class CheckRenders(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Checks to see if there are renders in the render directory for this version, if there are,
        """

        render_folder = os.path.dirname(alc.scene_object().copy(context='render').path_root)
        render_contents = os.listdir(render_folder)
        if render_contents:
            message = 'This version has renders, would you like to version up?'
            dialog = InputDialog(message=message, title='Renders Exist', buttons=['Ignore', 'Version Up'])
            dialog.exec_()
            if dialog.button == 'Version Up':
                alc.version_up()
                self.pass_check('Check Passed')
            elif dialog.button == 'Ignore':
                print('Ignoring Renders')
                self.pass_check('Check Passed')
            else:
                self.fail_check('Check Failed')
        else:
            self.pass_check('No Renders found, safe to continue')

