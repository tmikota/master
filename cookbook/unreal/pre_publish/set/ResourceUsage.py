import sys
import unreal
from PySide2 import QtWidgets, QtGui, QtUiTools, QtCore
from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.unreal_engine.ui.dialogs import ResourceDialog
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.unreal import alchemy as alc


class ResourceUsage(PreflightCheck):

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
        self.pass_check('Check Passed')
        # self.fail_check('Check Failed')
