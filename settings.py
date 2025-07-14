
class Settings:
    def __init__(self):
        self.game_field_dim = 3
        self.cell_size = 40
        self.hide_cells_percent = 25

        self.colors = {
            "canvas_bg": "#888888",
            "cell_bg": {
                "default": "#cccccc", 
                "hided": "#aaaaaa", 
                "selected": "#777777"
            },
        }

        self.square_gate = 3 # расстояние между квадратами NxN

        # для экрана выбора значения:
        self.button_width = 45 # примерная ширина кнопки с цифрой
        self.button_height = 40 # примерная высота кнопки

