from typing import Optional
from lib.frame import Frame
from src.views.intro import Introduction
from .users.index import UsersTable

class MainView(Frame):
    
    frameKey = "main_view"
    currentFrame = None

    def __init__(self, currentFrame:Optional[str] = None, *args, **kwargs):
        
        self.currentFrame: Optional[str] = currentFrame
        super().__init__(*args, **kwargs)


    def get_master(self):
        return self.get_frame('master')
    
    def create_widgets(self):
        self.clear_widgets()
        self.register_widget(Introduction())   
        
