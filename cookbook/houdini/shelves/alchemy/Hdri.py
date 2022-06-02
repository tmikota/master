def run():
        import hou
        import os

        from cgl.plugins.houdini.utils import get_hdri_json_path
        from cgl.core.utils.read_write import load_json

        choices = []
        selected = ''
        
        hdri_json = get_hdri_json_path()

        for filename in os.listdir(os.path.dirname(hdri_json)):
                if filename.endswith(".tx"):
                        choices.append(filename)
                        continue
                else:
                        continue

        selected = hou.ui.selectFromList(choices, 
        default_choices=(), 
        exclusive=True, 
        message=None, 
        title="HDRI Picker", 
        column_header="Choices", 
        num_visible_rows=10, 
        clear_on_cancel=False, 
        width=0, height=0)

        root = hou.node('/obj')
        node = root.createNode('rslightdome::2.0')

        node.parm('env_map').set(os.path.dirname(hdri_json)+'/'+choices[selected[0]])

        data=load_json(hdri_json)
        filename = os.path.splitext(choices[selected[0]])[0]
        
        rotation = data[filename]
        
        node.parm('ry').set(rotation)
