from lib.frame import Frame
from src.views.cars.index import CarsTable
from src.views.users.index import UsersTable

class SideBar(Frame):
    frameKey = 'sidebar'

    width = 20
    userTable = None

    def get_master(self):
        return self.get_frame('master')
    
    def create_widgets(self):
        self.configure(width=self.width, bg='lightgray', padx= 10)
        self.pack(side=self._tk.RIGHT, fill=self._tk.Y)
        # Add widgets specific to the SideBar
        label = self._tk.Label(self, text="پنل کنترل", width=self['width'])
        label.pack(pady=2)

        button1 = self._tk.Button(self, width=self.width, text="نمایش کاربران", command=self.create_users_table)
        button1.pack(pady=5)

        button2 = self._tk.Button(self, width=self.width, text="نمایش ماشین ها", command=self.create_cars_table)
        button2.pack(pady=5)

    def create_users_table(self):
        # mainFrame = cast(MainView, self.get_frame('main_view'))  # Cast to MainView
        # mainFrame.clear()
        mainView = self.get_frame('main_view')
        mainView.clear_widgets()
        mainView.register_widget(UsersTable())

    def create_cars_table(self):
        # mainFrame = cast(MainView, self.get_frame('main_view'))  # Cast to MainView
        # mainFrame.clear()
        mainView = self.get_frame('main_view')
        mainView.clear_widgets()
        mainView.register_widget(CarsTable())
        
        