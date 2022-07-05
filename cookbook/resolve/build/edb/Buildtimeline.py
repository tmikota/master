"""Buildtimeline.py

there is typically a alchemy.py, and utils.py file in the plugins directory.
look here for pre-built, useful functions
"""

from cgl.plugins.resolve import alchemy as alc
from cgl.plugins.preflight.preflight_check import PreflightCheck

class Buildtimeline(PreflightCheck):
    """Buildtimeline

    Args:
        PreflightCheck (_type_): _description_
    """
    def getName(self):
        """getName
        """
        return "Buildtimeline"

    def run(self):
        """
        script to be executed when the preflight is run.

        If the preflight is successful:
        self.pass_check('Message about a passed Check')

        if the preflight fails:
        self.fail_check('Message about a failed check')
        :return:
        """

        print("BuildTimeLine...")

        alchemy = alc.Alchemy()
        result = alchemy.build_load_timeline()

        if result:
            self.pass_check("Build Timeline Passed")
        else:
            self.fail_check('Build Timeline Failed')
