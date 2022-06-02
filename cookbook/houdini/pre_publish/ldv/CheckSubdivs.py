from cgl.plugins.preflight.preflight_check import PreflightCheck
from cgl.plugins.houdini import alchemy as alc
import hou

from cgl.plugins.houdini.alchemy import launch_preflight


class CheckSubdivs(PreflightCheck):
    so = alc.scene_object()
    max_subdivisions = so.project_settings['max_subdiv']
    if not max_subdivisions:
        max_subdivisions = 2

    def run(self):

        root = hou.node('/obj')

        for obj in root.children():
            error = self.check_subdivs(obj)
            if error:
                print('check_failed on {} check the subdivison nodes \
                depth to be less than {}'.format(obj, self.max_subdivisions))
            else:
                self.pass_check('Subdivs OK')

    def check_subdivs(self, obj):
        insideNodes = obj.allSubChildren()

        for node in insideNodes:
            if node.type().name() == 'subdivide':
                if node.parm('iterations').eval() > int(self.max_subdivisions):
                    # self.fail_check('Subdivs too high')

                    return 1
                else:
                    return 0
