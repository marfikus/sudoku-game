
from settings import Settings
from main_screen import MainScreen
from settings_screen import SettingsScreen
from input_screen import InputScreen


def main():
    settings = Settings()
    main_screen = MainScreen(settings)
    settings_screen = SettingsScreen(settings, main_screen)
    input_screen = InputScreen(main_screen)
    main_screen.start_game()


if __name__ == "__main__":
    main()

