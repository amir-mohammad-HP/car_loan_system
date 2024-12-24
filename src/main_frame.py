
from lib.frame import Frame
from .views.side_bar import SideBar
from .views.main_view import MainView

class MainFrame(Frame):
    _instance = None
    frameKey = 'master'
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MainFrame, cls).__new__(cls, frameKey=cls.frameKey)
        
        return cls._instance

    def __init__(self, master=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            super().__init__(master= master, title="Main Frame", bg='lightgray')
            self.create_main_widgets()
            self.initialized = True

    def create_main_widgets(self):
        self.clear_widgets()
        self.register_widget(SideBar())
        self.register_widget(MainView())
        

