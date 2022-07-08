import os
from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.nuke import alchemy as alc
import nuke
import glob
import traceback

PLATE_NODE_NAME = 'read_PLATE'
EDIT_REF_NODE_NAME = 'read_EREF'


class SetReadNodePaths(PreflightCheck):
    def getName(self):
        pass

    def run(self):
        """
        Finds read nodes ('read_PLATE and 'read_EREF') and sets paths according to latest published version
        """
        from importlib import reload

        import plugins.nuke.utils
        reload(plugins.nuke.utils)
        from plugins.nuke import utils

        try:
            utils.update_read_node(PLATE_NODE_NAME, task='plt')
            utils.update_read_node(EDIT_REF_NODE_NAME, task='edr')
        except:
            traceback.print_exc()
            self.fail_check('One or more read nodes have not been set, build step failed.')
            return

        self.pass_check('Read nodes have been set!')
