#
# 3DE4.script.name: build
#
# 3DE4.script.version:
#
# 3DE4.script.gui:  Main Window::alchemy
#
# 3DE4.script.gui.config_menus: true
#
from cgl.plugins.three_d_equalizer.alchemy import Alchemy


if __name__ == "__main__":
    Alchemy().build()
    print(">>> INFO - [build] Hello world!")
