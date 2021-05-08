from cgl.plugins.preflight.preflight_check import PreflightCheck
import cgl.plugins.maya.utils as utils
import pymel.core as pm


class CheckConstraints(PreflightCheck):

    def getName(self):
        pass

    @staticmethod
    def has_constraints(mesh):
        connections = pm.listConnections(mesh)
        for c in connections:
            if c.type() == 'parentConstraint':
                return True
        return False

    def run(self):
        """
        Finds any references that are constrained and puts them in the "ANIM" Group.
        """
        meshes = utils.get_reference_meshes()
        animated = pm.listRelatives('ANIM', children=True)
        for m in meshes:
            if self.has_constraints(m):
                if m not in animated:
                    pm.parent(m, 'ANIM')
        self.pass_check('Check Passed')
