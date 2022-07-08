import nuke
from collections import OrderedDict as odict
from cgl.plugins.preflight.preflight_check import PreflightCheck
from plugins.nuke import utils
from plugins.nuke.templates.config import TASK_BD_COLORS


# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
# from cgl.plugins.nuke import alchemy as alc

# Define task and node name pairs
SOURCE_TASKS = ('edr',          # Edit Ref Plate
                'lte',          # Lighting Render Layers
                'plt',          # Degrained Plate
                'plt_ingest',   # Original Plate
                'pnt',          # Paintout Plate
                'rep',          # Repo Transform Node
                'ret',          # Retime Plate and Kronos Node
                'rto',          # Roto Node (and Mattes ?)
                'cam',          # Camera FBX
                'trk',          # Undistort Node
                )

DX, DY = (100, 50)  # Grid W/H
BD_WIDTH, BD_HEIGHT = DX*5, DY*8  # Default Backdrop dimensions
ROW_HEIGHT = BD_HEIGHT + DY  # Default row height

TASK_SOURCES_LAYOUT = [
    ['edr', 'plt_ingest', 'plt', 'ret', 'pnt'],  # first row
    ['cam', 'lte', 'rto', 'rpo', 'trk']  # second row
]

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
        caret_x, caret_y = (0, 0)

        for row, tasks in enumerate(TASK_SOURCES_LAYOUT):
            for task in tasks:
                load_task_sources(task, posx, posy)




        read_nodes = nuke.allNodes('Read')
        camera_nodes = nuke.allNodes('Camera')

        for read_node in read_nodes:
            _task = read_node.name().split('_', 1)[-1]
            if '_' in _task:
                _task, _type = _task.split('_')
            utils.update_read_node(read_node, _task)

        # self.pass_check("Check Passed")
        # self.fail_check('Check Failed')
