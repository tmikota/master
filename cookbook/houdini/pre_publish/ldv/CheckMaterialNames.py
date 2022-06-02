from cgl.plugins.preflight.preflight_check import PreflightCheck
import os
import cgl.plugins.houdini.alchemy as alc
from cgl.core.utils.general import save_json, load_json
from cgl.core.path import PathObject
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.houdini import alchemy as alc
import hou 

class CheckMaterialNames(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        """
        if any @path shape doesn't have an @shot material path put it in a list, throw up a magic list of all of them, fail the test.
        """
        list = []

        for geo in hou.node('obj').children():
            for node in geo.children():
                if node.type().name() == 'alembic':
                    output = node.outputs()[0].type().name()
                    if not output == 'material':
                        list.append(geo.name())

        if len(list) > 0:
            self.fail_check('Missing materials:' + str(list))
        else:
            self.pass_check('Check Passed')