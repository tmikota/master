import sys
import os

sys.path.append( os.getenv("USERPROFILE") + R"\PycharmProjects\cglumberjack\python\cglumberjack" )
from cgl.plugins.resolve import alchemy as alc

from Qt import  QtWidgets
print(sys.path)
print(alc.__file__)
# global window
def run():
    print("Color: Test")
    try:
        alchemy  = alc.Alchemy()
        scene_object.get_scene_name()
        print(scene_object)
    except Exception as e:
        print(e)