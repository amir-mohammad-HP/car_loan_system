import logging
import os
import tkinter as tk
from src.main_frame import MainFrame
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    filename=log_file_path,
    filemode='a'
)

class App:
    def __init__(self):
        self.build()

    def build(self): 
        self.root = tk.Tk()
        self.root.title("Car Loan Service")
        self.root.geometry("800x400")
        self.main_frame = MainFrame(self.root)
        return self
    
    def mainloop(self):
        logging.info('Starting application...')
        self.root.mainloop()
    
    def destroy(self):
        logging.info('Destroying application...')
        self.root.destroy()

def run_app():
    logging.info('Initialize application...')
    app = App()
    return app

if __name__ == "__main__":
    module_name = __name__

    logging.info('Initializing application...')
    app = run_app()  
    app.mainloop()