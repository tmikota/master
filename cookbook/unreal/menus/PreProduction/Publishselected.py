# from cgl.plugins.unreal import alchemy as alc
import cgl.plugins.unreal_engine.utils as utils


def run():
    """
    publishes the selected mdl, bundle or layout.
    """
    utils.publish_selected()