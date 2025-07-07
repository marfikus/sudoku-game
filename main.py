
from game_field import GameField


def main():
    gf = GameField(3)
    gf.print_game_field()

    gf.mix_game_field()
    gf.print_game_field()

    gf.hide_cells_in_game_field(25)
    gf.print_game_field()

    gf.solve_game_field()
    gf.print_game_field()


if __name__ == "__main__":
    main()

