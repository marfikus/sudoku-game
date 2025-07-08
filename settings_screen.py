
from tkinter import BooleanVar, Toplevel, Checkbutton


class SettingsScreen:
    def __init__(self, settings, main_screen):
        self.settings = settings
        self.settings_screen = None
        self.settings_screen_is_active = False
        self.main_screen = main_screen
        self.main_screen.link_to_mainmenu(self)


    def show(self):
        if self.settings_screen_is_active:
            return

        self.settings_screen = Toplevel()
        x = self.main_screen.root.winfo_x()
        y = self.main_screen.root.winfo_y()
        self.settings_screen.geometry(f"+{x}+{y}")
        self.settings_screen.title("Settings")
        self.settings_screen.resizable(False, False)
        self.settings_screen.protocol("WM_DELETE_WINDOW", self.close)
        self.settings_screen_is_active = True


    def update_settings(self):
        pass


    def close(self):
        self.settings_screen.destroy()
        self.settings_screen_is_active = False


