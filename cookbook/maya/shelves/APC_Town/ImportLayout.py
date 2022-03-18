import cgl.plugins.maya.tasks.lay as lay
from importlib import reload
reload(lay)

def run():
    lay.Task().import_latest(seq='Environment', shot='backgroundD', scope='assets')

