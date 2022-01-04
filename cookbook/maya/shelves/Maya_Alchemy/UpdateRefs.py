import cgl.plugins.maya.utils as utils


def run():
    """
    UPdates all references in the scene, or if there are references with the incorrect root, it will replace it
    with the root from this computer.
    """
    utils.update_all_references()

