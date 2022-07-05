# from cgl.plugins.resolve import alchemy as alc
from davinci_resolve_tools.utils.marz_resolve_scripts import MarzResolveScripts
mrs = MarzResolveScripts.get_instance()


def run():
    print("hello world: Loadproject Gui")
    mrs.load_project()
