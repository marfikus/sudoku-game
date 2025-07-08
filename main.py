
from settings import Settings
from settings_screen import SettingsScreen
from main_screen import MainScreen


def main():
    # gf = GameField(3)
    # gf.print_game_field()

    # gf.mix_game_field()
    # gf.print_game_field()

    # gf.hide_cells_in_game_field(25)
    # gf.print_game_field()

    # gf.solve_game_field()
    # gf.print_game_field()

    settings = Settings()
    main_screen = MainScreen(settings)
    settings_screen = SettingsScreen(settings, main_screen)
    main_screen.start_game()


if __name__ == "__main__":
    main()

