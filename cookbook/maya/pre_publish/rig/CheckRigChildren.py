from cgl.plugins.preflight.preflight_check import PreflightCheck
# there is typically a alchemy.py, and utils.py file in the plugins directory.
# look here for pre-built, useful functions
import pymel.core as pm
from cgl.ui.widgets.dialog import MagicList
import cgl.plugins.maya.utils as utils


class CheckRigChildren(PreflightCheck):

    def getName(self):
        pass

    def run(self):
        childs_names = []
        for each in pm.listRelatives('rig', children=True):
            childs_names.append(str(each))
        missing = utils.check_child_naming(selected='rig', children=['geo', 'controls'])
        print('missing', missing)
        if missing:
            message = "I found the above, I'm expecting: 'geo' and 'controls'"
            dialog = MagicList(title="Illegally Named Rig Children", message=message,
                               list_items=childs_names, buttons=[], auto_close=False,
                               on_selection=self.select_list)
            dialog.exec_()
            self.fail_check("Improperly named children of Rig")
        else:
            self.pass_check("Found Geo and Controls as children of Rig")

    def select_list(self, data):
        pm.select(d=True)
        for d in data:
            self.items.append(d)
            pm.select(d, add=True)
