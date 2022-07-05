import nuke
from cgl.plugins.preflight.preflight_check import PreflightCheck
from plugins.nuke import utils


# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.nuke import alchemy as alc

# Define task and node name pairs
SOURCE_TASKS = ('edr',          # Edit Ref
                'lte',          # Lighting Renders
                'plt',          # Degrained Plate
                'plt_ingest',   # Original Plate
                'pnt',          # Paintout
                'rep',          # Repo Node
                'ret',          # Retime Plate
                'rto',          # Roto Node
                'trk',          # Tracked Camera
                )



class SetSourceNodePaths(PreflightCheck):
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
        print("Updating Comp Source Nodes")

        read_nodes = nuke.allNodes('Read')
        camera_nodes = nuke.allNodes('Camera')

        for read_node in read_nodes:
            _task = read_node.name().split('_', 1)[-1]
            if '_' in _task:
                _task, _type = _task.split('_')
            utils.update_read_node(read_node, _task)

        # self.pass_check("Check Passed")
        # self.fail_check('Check Failed')
