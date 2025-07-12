
from tkinter import Toplevel, Frame, Button, LEFT


class InputScreen:
    def __init__(self, main_screen):
        self.screen = None
        self.screen_is_active = False
        self.main_screen = main_screen
        self.main_screen.input_screen = self


    def show(self, cell_value, game_field_dim):
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

        digit = 1
        for y in range(game_field_dim):
            f_row = Frame(self.screen)
            for x in range(game_field_dim):
                Button(
                    f_row, 
                    text=digit, 
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


