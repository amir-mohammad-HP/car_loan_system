from typing import Literal, Optional
from lib.frame import Frame

class Introduction(Frame):
    
    frameKey = "introduction"

    def get_master(self):
        return self.get_frame('master')
    
    def create_widgets(self):

        # self.configure(width='100%', bg='lightgray', padx= 40)
        self.pack(side=self._tk.RIGHT, fill=self._tk.BOTH, expand=True)
        
        self.label = self._tk.Label(self, text="WellCome", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.label = self._tk.Label(self, text="Amir Mohammad Hamidi Pour", font=("Arial", 18))
        self.label.pack(pady=20)

        self.label = self._tk.Label(self, text="4011232223", font=("Arial", 14))
        self.label.pack(pady=10)
