from cgl.plugins.preflight.preflight_check import PreflightCheck

# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc

import nuke


class SetWriteNodePath(PreflightCheck):
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
        print("PreflightTemplate - SetWriteNodePath")
        try:
            so = alc.scene_object()
            write_node_name = f'write_{so.task}'
            updated_write_node = alc.update_write_node(nuke.toNode(write_node_name))
            self.shared_data['nuke_write_node'] = updated_write_node
        except:
            self.fail_check('Check Failed. Could not find Write node')
            return
        self.pass_check("Write node path has been set.")
