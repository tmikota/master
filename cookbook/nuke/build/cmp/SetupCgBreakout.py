from cgl.plugins.preflight.preflight_check import PreflightCheck
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
from cgl.plugins.nuke import alchemy as alc
from importlib import reload
reload(alc)

TASKS = ['lte']


class SetupCgBreakout(PreflightCheck):
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
        print("PreflightTemplate SetupCgBreakout")
        import nuke
        from cgl.plugins.nuke import aov_breakout
        read_nodes = nuke.allNodes('Read')
        break_out = False
        read_node_found = False
        for read_node in read_nodes:

            _task = read_node.name().split('_', 1)[-1]
            if '_' in _task:
                _task, _type = _task.split('_')
            if _task not in TASKS:
                continue
            if not read_node['file'].value():
                continue
            read_node_found = True
            break_out = aov_breakout.assemble_aov_breakout(read_node)

        if break_out:
            self.pass_check("Check Passed")
        else:
            if not read_node_found:
                log.error('ERROR: Could not find read node with %s in name or it\'s missing an image file' % TASKS)
            self.fail_check('Check Failed. Check Script Editor for details')
