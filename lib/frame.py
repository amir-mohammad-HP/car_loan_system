import logging
import tkinter as tk
from typing import Callable, Dict, List, Optional
from venv import logger

class Frame(tk.Frame):
    _tk = tk
    _frameMemo: Dict[str, 'Frame'] = {}  # Change to store Frame instances
    frameKey = None
    master: Optional[tk.Widget] = None
    _widget_pointer: Dict[str, List['Frame']] = {}

    def __new__(cls, *args, **kwargs):
        frameKey = kwargs.get('frameKey', None)
        if not frameKey:
            frameKey = cls.frameKey

        if not frameKey:
            raise Exception('frameKey must be provided')

        return super(Frame, cls).__new__(cls)

    def __init__(self, frameKey=None, master=None, title="Frame", **kwargs):
        super().__init__(master, **kwargs)
        logging.info(f'create {[self.frameKey]}')
        if frameKey:
            self.frameKey = frameKey 
        
        if not self.frameKey:
            raise Exception('frameKey must be provided')
        
        self.add_frame(self.frameKey, self)

        self.title = title
        self.create_widgets()

    @classmethod
    def add_frame(cls, key: str, frame: 'Frame'):
        if key in cls._frameMemo:
            return
        cls._frameMemo[key] = frame

    @classmethod
    def get_frame(cls, key: str) -> 'Frame':
        frame = cls._frameMemo.get(key, None)
        if not frame:
            raise Exception('frame {} does not exist!'.format(key))
        return frame

    @classmethod
    def remove_frame(cls, key: str):
        logger.debug('remove frame ' + key)
        if key in cls._frameMemo:
            logger.debug(f'frame {key} in frameMemo Found')
            frame = cls._frameMemo[key]
            frame.destroy()
            logger.debug(f'frame {key} destroyed')
            if key in cls._frameMemo:
                cls._frameMemo.pop(key)
            
                logger.debug(f'frame {key} removed from frameMemo')
            else:
                print(f"Key '{key}' not found in _frameMemo.")

    @classmethod
    def list_frames(cls):
        return cls._frameMemo.keys()

    def register_callback(self, callback: Callable[['Frame'], None]) -> None:
        '''
        accept callback , 
        callback get the instance of current frame and let use to define registeration widget
        '''
        if self.frameKey:
            callback(self.get_frame(self.frameKey))

    def register_widget(self, frame: 'Frame'):
        '''
        register a widget to remmember it , incase to use on other instances indirectly
        '''
        logger.info('register frame key: ' + str(self.frameKey))
        if (self.frameKey):
            widgets = self._widget_pointer.get(self.frameKey)
            if (type(widgets) == list):
                widgets.append(frame)
            else:
               self._widget_pointer[self.frameKey] = [frame]
        return self

    def clear_widgets(self):
        if (self.frameKey):
            widgets = self._widget_pointer.get(self.frameKey)
            widgets = widgets if widgets else []
            for w in widgets:
                w.destroy()
                del w

    def create_widgets(self):
        pass
    
    