
from tkinter import Toplevel, Frame, Button, LEFT


class InputScreen:
    def __init__(self, settings, main_screen):
        self.screen = None
        self.screen_is_active = False
        self.settings = settings
        self.main_screen = main_screen
        self.main_screen.input_screen = self


    def show(self, cell_value, game_field_dim):
        if self.screen_is_active:
            return

        self.screen = Toplevel()
        self.screen.overrideredirect(True)
        # self.screen.title("Select action")
        # self.screen.resizable(False, False)
        self.screen.protocol("WM_DELETE_WINDOW", self.close)

        # расположение по центру главного окна
        root_x = self.main_screen.root.winfo_x()
        root_y = self.main_screen.root.winfo_y()
        root_w = self.main_screen.root.winfo_width()
        root_h = self.main_screen.root.winfo_height()
        root_center_x = root_x + (root_w // 2)
        root_center_y = root_y + (root_h // 2)
        # сделал так, поскольку размеры текущего окна ещё не определены
        # (а если позже это делать, то будет заметно мелькание окна при изменении позиции)
        # поэтому просто рассчитываю предполагаемые размеры окна и использую их
        future_screen_w = game_field_dim * self.settings.button_width
        future_screen_h = (game_field_dim + 1) * self.settings.button_height
        x = root_center_x - (future_screen_w // 2)
        y = root_center_y - (future_screen_h // 2)
        self.screen.geometry(f"+{x}+{y}")

        self.screen_is_active = True

        digit = 1
        for y in range(game_field_dim):
            f_row = Frame(self.screen)
            for x in range(game_field_dim):
                Button(
                    f_row, 
                    text=digit, 
                    width=2, 
                    command=lambda digit=digit: self.click_digit(digit)
                ).pack(side=LEFT)
                digit += 1
            f_row.pack()

        f_row = Frame(self.screen)
        Button(
            f_row, 
            text="Clear",
            command=self.click_clear
        ).pack(side=LEFT)
        Button(
            f_row, 
            text="Cancel",
            command=self.click_cancel
        ).pack(side=LEFT)
        f_row.pack()


    def click_digit(self, digit):
        print(digit)


    def click_clear(self):
        print("clear")


    def click_cancel(self):
        print("cancel")


    def close(self):
        self.screen.destroy()
        self.screen_is_active = False


