from cgl.plugins.Qt import QtCore, QtGui, QtWidgets
import webbrowser
import pymel.core as pm
from cgl.plugins.maya.tasks.tex import create_and_attach_shader
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class Colorizer(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(Colorizer, self).__init__(parent)
        self.setWindowTitle('Color-o-matic')
        layout = QtWidgets.QVBoxLayout(self)
        color_reference_button = QtWidgets.QPushButton('Color Reference')
        grid_layout = QtWidgets.QGridLayout()
        # button_layout = QtWidgets.QHBoxLayout()
        # ok_button = QtWidgets.QPushButton('Create Shaders')
        # cancel_button = QtWidgets.QPushButton('Cancel')
        # button_layout.addStretch(1)
        # button_layout.addWidget(cancel_button)
        # button_layout.addWidget(ok_button)
        materials = ['base', 'secondary', 'accent', 'trimA', 'trimB']
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
            combo.addItems(['default', 'gold', 'silver', 'copper', 'bronze', 'steel'])
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
        # todo - do something here to make the corresponding button change color according to the "metallic" shader.

    # def create_and_connect_shaders(self):
    #     for shader in self.shaders:
    #         shader_label = shader.text()
    #         shader_color = shader.color
    #         shader_type = shader.type
    #
    #         print(shader_label)
    #         if shader_color:
    #             create_and_attach_shader(name=shader_label, hex_color=shader_color)

    @staticmethod
    def color_reference_clicked():
        webbrowser.open('https://coolors.co/palettes/trending')

    def on_color_changed(self):
        line_edit_text = self.sender().text()
        button = self.sender().shader
        button.color = line_edit_text
        button.setStyleSheet('background-color: #{};'.format(line_edit_text))
        print('Changing {} to {}'.format(button.text(), line_edit_text))
        create_and_attach_shader(button.text(), line_edit_text)


def hex_to_rgb(hex):
    r, g, b = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
    return r/255, g/255, b/255


def create_and_attach_shader(name, hex_color):
    mtl_name = '{}_shd'.format(name)
    if pm.objExists(mtl_name):
        pm.delete(mtl_name)
    sg_name = '{}_SG'.format(name)
    if pm.objExists(sg_name):
        pm.delete(sg_name)
    shader = pm.shadingNode(str('aiStandardSurface'), asShader=True, name=mtl_name)
    if not pm.objExists(sg_name):
        pm.sets(renderable=True, noSurfaceShader=True, empty=True, name=sg_name)
        pm.connectAttr('%s.outColor' % shader, '%s.surfaceShader' % sg_name)
    pm.select(d=True)
    mtl_groups = pm.ls(regex='*{}_mtl'.format(name))
    pm.select(mtl_groups)
    pm.sets(sg_name, forceElement=True)
    pm.select(d=True)
    r, g, b = hex_to_rgb(hex_color)
    pm.setAttr('{}.baseColor'.format(mtl_name), r, g, b, type='double3')


def run():
    dialog = Colorizer()
    dialog.show()

