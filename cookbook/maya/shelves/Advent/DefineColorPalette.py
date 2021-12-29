from cgl.plugins.Qt import QtCore, QtGui, QtWidgets
import webbrowser
import time
import pymel.core as pm
from cgl.plugins.maya.tasks.tex import create_and_attach_shader
from cgl.plugins.maya.tasks.shd import get_default_shader
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class Colorizer(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(Colorizer, self).__init__(parent)
        self.setWindowTitle('Color-o-matic')
        self.default_shader = get_default_shader()

        layout = QtWidgets.QVBoxLayout(self)
        color_reference_button = QtWidgets.QPushButton('Color Reference')
        grid_layout = QtWidgets.QGridLayout()
        materials = ['base', 'secondary', 'accent', 'trimA', 'trimB', 'special']
        self.shaders = []
        for i, m in enumerate(materials):
            label = QtWidgets.QPushButton(m)
            label.color = ''
            self.shaders.append(label)
            line_edit = QtWidgets.QLineEdit()
            line_edit.label = m
            line_edit.shader = label
            combo = QtWidgets.QComboBox()
            combo.label = m
            combo.shader = label
            combo.line_edit = line_edit
            combo.addItems(['default', 'gold', 'chrome'])
            label.type = 'default'
            grid_layout.addWidget(label, i, 0)
            grid_layout.addWidget(line_edit, i, 1)
            grid_layout.addWidget(combo, i, 2)

            label.clicked.connect(self.on_shader_clicked)
            line_edit.textChanged.connect(self.on_color_changed)
            combo.currentIndexChanged.connect(self.on_combo_changed)

        layout.addWidget(color_reference_button)
        layout.addLayout(grid_layout)
        # layout.addLayout(button_layout)

        color_reference_button.clicked.connect(self.color_reference_clicked)
        # ok_button.clicked.connect(self.create_and_connect_shaders)

    def on_shader_clicked(self):
        name = self.sender().text()
        pm.select(d=True)
        mtl_groups = pm.ls(regex='*{}_mtl'.format(name))
        pm.select(mtl_groups)

    def on_combo_changed(self):
        combo = self.sender()
        combo.shader.type = combo.currentText()
        if combo.currentText() == 'default':
            if combo.line_edit.text():
                create_and_attach_shader(combo.shader.text(), combo.line_edit.text(), source_shader=self.default_shader,
                                         shader_type=combo.currentText())
            else:
                print('need hex value to create shader')
        else:
            mtl = combo.shader.text()
            source_shader = self.default_shader
            shader_type = combo.currentText()
            create_and_attach_shader(name=mtl, hex_color='', source_shader=source_shader,
                                     shader_type=shader_type)

    def default_selected(self):
        print(self.sender().button.shader)
        print('its default')

    @staticmethod
    def color_reference_clicked():
        webbrowser.open('https://coolors.co/palettes/trending')

    def on_color_changed(self):
        line_edit_text = self.sender().text()
        button = self.sender().shader
        button.color = line_edit_text
        button.setStyleSheet('background-color: #{};'.format(line_edit_text))
        print('Changing {} to {}'.format(button.text(), line_edit_text))
        create_and_attach_shader(button.text(), line_edit_text, source_shader=self.default_shader)


def hex_to_rgb(hex):
    r, g, b = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    return r/255, g/255, b/255


def rgb_to_hex(r, g, b):
    print(r, g, b)


def create_and_attach_shader(name, hex_color, source_shader, shader_type='default'):

    mtl_name = '{}_shd'.format(name)
    if pm.objExists(mtl_name):
        pm.delete(mtl_name)
    sg_name = '{}_SG'.format(name)
    if pm.objExists(sg_name):
        pm.delete(sg_name)
    shader = pm.shadingNode(str(source_shader), asShader=True, name=mtl_name)
    if not pm.objExists(sg_name):
        pm.sets(renderable=True, noSurfaceShader=True, empty=True, name=sg_name)
        pm.connectAttr('%s.outColor' % shader, '%s.surfaceShader' % sg_name)
    pm.select(d=True)
    mtl_groups = pm.ls(regex='*{}_mtl'.format(name))
    pm.select(mtl_groups)
    pm.sets(sg_name, forceElement=True)
    pm.select(d=True)
    if shader_type == 'default':
        r, g, b = hex_to_rgb(hex_color)
        if source_shader == 'RedshiftMaterial':
            pm.setAttr('{}.diffuse_color'.format(mtl_name), r, g, b, type='double3')
        else:
            pm.setAttr('{}.baseColor'.format(mtl_name), r, g, b, type='double3')
        return
    elif shader_type == 'gold':
        pm.select(mtl_name)
        pm.setAttr('{}.preset'.format(mtl_name), 5)
        print('pm.setAttr("{}.preset", 5)'.format(mtl_name))
        return
    elif shader_type == 'silver':
        pm.setAttr('{}.preset'.format(mtl_name), 9)
        # button.setStyleSheet('background-color: #{};'.format(line_edit_text))
    elif shader_type == 'chrome':
        pm.select(mtl_name)
        print('pm.setAttr("{}.preset", 9)'.format(mtl_name))
        pm.setAttr('{}.preset'.format(mtl_name), 9)
        pm.setAttr('{}.refl_roughness'.format(mtl_name), .1)
        return
    elif shader_type == 'copper':
        pm.setAttr('{}.preset'.format(mtl_name), 4)
        pm.setAttr('{}.refl_roughness'.format(mtl_name), .25)
        pm.setAttr('{}.refl_reflectivity'.format(mtl_name), 0.7215, 0.4509, 0.2, type='double3')
    elif shader_type == 'iron':
        pm.setAttr('{}.preset'.format(mtl_name), 6)
    elif shader_type == 'lead':
        pm.setAttr('{}.preset'.format(mtl_name), 7)
    elif shader_type == 'platinum':
        pm.setAttr('{}.preset'.format(mtl_name), 8)


def run():
    dialog = Colorizer()
    dialog.show()

