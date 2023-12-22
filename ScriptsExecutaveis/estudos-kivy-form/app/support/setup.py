import platform
from kivy.core.window import Window

class Setup():
    def __init__(self):
        if platform.system() == "Windows":
            Window.size = (800, 200)
        else:
            pass