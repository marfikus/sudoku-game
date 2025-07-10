
from tkinter import Tk, Canvas, Menu, CENTER
import random

from game_field import GameField


colors = {
    "red": ["#ff0000", "#900000"],
    "green": ["#00ff00", "#009000"],
    "blue": ["#0000ff", "#000090"],
    "gray": ["#aaaaaa", "#dddddd"],
}

class MainScreen:
    def __init__(self, settings):
        self.settings = settings
        self.settings_screen = None

        self.root = Tk()
        self.root.title("Sudoku game")
        self.root.resizable(False, False)

        self.mainmenu = Menu(self.root)
        self.root.config(menu=self.mainmenu)
        self.mainmenu.add_command(label="New game", command=self.start_game)
        self.mainmenu.add_command(label="Settings", command=self.show_settings)

        self.width = None
        self.height = None
        self.game_field = None
        self.c = None
        self.game_is_active = False


    def link_to_mainmenu(self, settings_screen):
        self.settings_screen = settings_screen


    def start_game(self):
        if self.game_is_active:
            self.c.destroy()
            self.game_is_active = False
            if self.settings_screen.settings_screen_is_active:
                self.settings_screen.close()

        self.game_field = GameField(self.settings.game_field_dim)
        self.game_field.hide_cells(self.settings.hide_cells_percent)
        # self.game_field.solve()
        self.game_field.show()

        self.width = self.settings.cell_size * self.game_field.size
        self.height = self.settings.cell_size * self.game_field.size

        self.c = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.c.pack()

        x = 0
        y = 0
        for h in range(self.game_field.size):
            for w in range(self.game_field.size):                
                cell_color = colors["gray"][0]
                matrix_value = self.game_field.matrix[h][w]
                screen_value = matrix_value

                if matrix_value == 0:
                    screen_value = ""
                    cell_color = colors["gray"][1]

                rect = self.c.create_rectangle(x, y, 
                    x + self.settings.cell_size, 
                    y + self.settings.cell_size, 
                    fill=cell_color
                )

                x_center = x + self.settings.cell_size / 2
                y_center = y + self.settings.cell_size / 2
                text = self.c.create_text(
                    x_center, 
                    y_center, 
                    text=screen_value, 
                    justify=CENTER
                )

                if matrix_value == 0:
                    block = {"rect": rect, "text": text}
                    # print(self.game_field.hided_cells[f"{h} {w}"])
                    self.game_field.hided_cells[f"{h} {w}"]["screen_block"] = block

                x += self.settings.cell_size

            x = 0
            y += self.settings.cell_size

        # print(len(self.game_field.hided_cells), self.game_field.hided_cells)

        self.c.bind("<Button-1>", self.click_cell)

        self.game_is_active = True
        self.root.mainloop()


    def show_settings(self):
        self.settings_screen.show()


    def click_cell(self, event):
        pass

