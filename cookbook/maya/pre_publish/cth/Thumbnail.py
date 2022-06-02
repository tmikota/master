from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.maya.alchemy import screen_grab
from cgl.ui.widgets.dialog import InputDialog


class Thumbnail(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        Creates a thumbnail within the current maya scene.
        """
        dialog = InputDialog(title='Create Thumbnail', message='Click Ok to drag a rectangle around the thumbnail area')
        dialog.exec_()

        if dialog.button == 'Ok':
            screen_grab()
            self.pass_check('Thumbnail Created')
        else:
            self.fail_check('No thumb Created')
