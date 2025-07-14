
class Settings:
    def __init__(self):
        self.game_field_dim = 3 # размерность игрового поля, возможные значения: 2, 3, 4, 5
        self.cell_size = 40 # размер ячейки игрового поля
        self.hide_cells_percent = 25 # процент скрываемых чисел (уровень сложности)

        self.colors = { # цвета, используемые в интерфейсе
            "canvas_bg": "#888888", # фон канваса
            "cell_bg": {
                "default": "#cccccc", # фон обычной ячейки
                "hided": "#aaaaaa", # фон скрытой ячейки
                "selected": "#777777" # фон выбранной ячейки
            },
        }

        self.square_gap = 3 # расстояние между квадратами NxN

        # для экрана выбора значения:
        self.button_width = 45 # примерная ширина кнопки с цифрой
        self.button_height = 40 # примерная высота кнопки

