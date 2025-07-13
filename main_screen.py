
import tkinter as tk
import random

from game_field import GameField


class MainScreen:
    def __init__(self, settings):
        self.settings = settings
        self.settings_screen = None
        self.input_screen = None

        self.root = tk.Tk()
        self.root.title("Sudoku game")
        self.root.resizable(False, False)

        self.mainmenu = tk.Menu(self.root)
        self.root.config(menu=self.mainmenu)
        self.mainmenu.add_command(label="New game", command=self.start_game)
        self.mainmenu.add_command(label="Settings", command=self.show_settings)

        self.width = None
        self.height = None
        self.game_field = None
        self.c = None
        self.game_is_active = False
        self.selected_cell = None


    def start_game(self):
        if self.game_is_active:
            self.c.destroy()
            self.game_is_active = False

            if self.settings_screen.screen_is_active:
                self.settings_screen.close()

            if self.input_screen.screen_is_active:
                self.input_screen.close()

        self.game_field = GameField(self.settings.game_field_dim)
        self.game_field.hide_cells(self.settings.hide_cells_percent)
        # self.game_field.solve()
        self.game_field.show()

        self.width = self.settings.cell_size * self.game_field.size
        self.height = self.settings.cell_size * self.game_field.size

        self.c = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.c.pack()

        x = 0
        y = 0
        for h in range(self.game_field.size):
            for w in range(self.game_field.size):                
                cell_color = self.settings.colors["cell_bg"]["default"]
                matrix_value = self.game_field.matrix[h][w]
                screen_value = matrix_value

                if matrix_value == 0:
                    screen_value = ""
                    cell_color = self.settings.colors["cell_bg"]["hided"]

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
                    justify=tk.CENTER
                )

                if matrix_value == 0:
                    block = {"rect": rect, "text": text}
                    self.game_field.hided_cells[f"{h} {w}"]["screen_block"] = block

                x += self.settings.cell_size

            x = 0
            y += self.settings.cell_size

        self.c.bind("<Button-1>", self.click_cell)

        self.game_is_active = True
        self.root.mainloop()


    def show_settings(self):
        self.settings_screen.show()


    def click_cell(self, event):
        for cell in self.game_field.hided_cells:
            rect = self.game_field.hided_cells[cell]["screen_block"]["rect"]
            coords = self.c.coords(rect)
            if (coords[0] <= event.x <= coords[2]) and (coords[1] <= event.y <= coords[3]):
                # print(self.game_field.hided_cells[cell])
                self.selected_cell = cell
                self.c.itemconfig(rect, fill=self.settings.colors["cell_bg"]["selected"])
                self.input_screen.show(
                    self.game_field.hided_cells[cell]["input_value"]
                )
                break


    def change_cell_value(self, digit):
        rect = self.game_field.hided_cells[self.selected_cell]["screen_block"]["rect"]
        self.c.itemconfig(rect, fill=self.settings.colors["cell_bg"]["hided"])

        if digit is not None:
            text = self.game_field.hided_cells[self.selected_cell]["screen_block"]["text"]
            
            if digit == 0: # click Clear
                self.c.itemconfig(text, text="")
            else: # click digit
                self.c.itemconfig(text, text=digit)

            self.game_field.hided_cells[self.selected_cell]["input_value"] = digit
            y, x = self.game_field.hided_cells[self.selected_cell]["matrix_coords"]
            self.game_field.matrix[y][x] = digit

        # check game field

