
from tkinter import BooleanVar, Toplevel, Checkbutton


class SettingsScreen:
    def __init__(self, settings, main_screen):
        self.settings = settings
        self.screen = None
        self.screen_is_active = False
        self.main_screen = main_screen
        self.main_screen.settings_screen = self


    def show(self):
        if self.screen_is_active:
            return

        self.screen = Toplevel()
        x = self.main_screen.root.winfo_x()
        y = self.main_screen.root.winfo_y()
        self.screen.geometry(f"+{x}+{y}")
        self.screen.title("Settings")
        self.screen.resizable(False, False)
        self.screen.protocol("WM_DELETE_WINDOW", self.close)
        self.screen_is_active = True


    def update_settings(self):
        pass


    def close(self):
        self.screen.destroy()
        self.screen_is_active = False


