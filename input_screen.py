
from tkinter import Toplevel


class InputScreen:
    def __init__(self, main_screen):
        self.screen = None
        self.screen_is_active = False
        self.main_screen = main_screen
        self.main_screen.input_screen = self


    def show(self, cell_value):
        if self.screen_is_active:
            return

        self.screen = Toplevel()
        x = self.main_screen.root.winfo_x()
        y = self.main_screen.root.winfo_y()
        self.screen.geometry(f"+{x}+{y}")
        self.screen.title("Select action")
        self.screen.resizable(False, False)
        self.screen.protocol("WM_DELETE_WINDOW", self.close)
        self.screen_is_active = True


    def close(self):
        self.screen.destroy()
        self.screen_is_active = False


