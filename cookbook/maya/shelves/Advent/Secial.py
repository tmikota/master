from cgl.plugins.maya.utils import get_shape_name
import pymel.core as pm


def create_shader_tag(tag='special'):
    selected = pm.ls(sl=True)
    if selected:
        for s in selected:
            shp = get_shape_name(s)
            try:
                pm.addAttr(shp, ln="shader_tag", dt="string")
            except RuntimeError:
                print('attr "shader_tag" exists')
            pm.setAttr('{}.shader_tag'.format(shp), tag)
    else:
        print('Please select something and try again')


def run():
    create_shader_tag()