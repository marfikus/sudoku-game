
class Settings:
    def __init__(self):
        self.game_field_dim = 3
        self.cell_size = 40
        self.hide_cells_percent = 25

        self.colors = {
            "cell_bg": {
                "default": "#cccccc", 
                "hided": "#aaaaaa", 
                "selected": "#777777"
            },
        }

        # для экрана выбора значения:
        self.button_width = 45 # примерная ширина кнопки с цифрой
        self.button_height = 40 # примерная высота кнопки

