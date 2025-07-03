
import random, copy


game_field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def print_game_field():
    print("\n===========================\n")

    for i in game_field:
        print(i)

    print("\n===========================\n")


def detect_square(string, column):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    string = int(string)
    column = int(column)

    if string <= 2:
        y1 = 0
        y2 = 2
    
    elif string > 2 and string <= 5:
        y1 = 3
        y2 = 5
    
    elif string > 5:
        y1 = 6
        y2 = 8

    if column <= 2:
        x1 = 0
        x2 = 2

    elif column > 2 and column <= 5:
        x1 = 3
        x2 = 5

    elif column > 5:
        x1 = 6
        x2 = 8

    return (x1, y1, x2, y2)


def create_unique_set(string, column):

    if game_field[string][column] != 0:
        return set()

    all_numbers = set(range(1, 10))
    exist_numbers = set()

    our_square = detect_square(string, column)
    x1 = our_square[0]
    y1 = our_square[1]
    x2 = our_square[2] + 1
    y2 = our_square[3] + 1

    for i in range(0, 9):
        x = game_field[string][i]
        if x != 0:
            exist_numbers.add(x)

        y = game_field[i][column]
        if y != 0:
            exist_numbers.add(y)

    for i in range(y1, y2):
        for j in range(x1, x2):
            n = game_field[i][j]
            if n != 0:
                exist_numbers.add(n)

    unique_set = all_numbers - exist_numbers

    # return all_numbers, exist_numbers, unique_set
    return unique_set


def fill_game_field():
    def calc_value(value):
        if value > 9:
            return value - 9
        return value

    block_start = 1
    str_start = 1

    # по блокам из 3х строк:
    for i in range(0, 8, 3):
        str_start = block_start
        # по строкам:
        for j in range(i, i + 3):
            # по ячейкам:
            for n in range(0, 9):
                game_field[j][n] = calc_value(str_start + n)

            str_start += 3
        block_start += 1


def mix_game_field():
    # global game_field

    def transpose(): # not used
        list_of_columns = []
        # по столбцам:
        for j in range(len(game_field)):
            # берем j-тую ячейку каждой строки:
            column = [game_field[i][j] for i in range(len(game_field))]
            list_of_columns.append(column)
        
        return list_of_columns

    def mix_strings(): # not used
        mixed = []
        variants = list(range(len(game_field)))
        for i in range(len(game_field)):
            n = random.choice(variants)
            mixed.append(game_field[n])
            variants.remove(n)

        return mixed

    def create_blocks_view(mode):
        global game_field

        block = []
        result = []

        for n in range(0, 9, 3):
            for m in range(3):
                if mode == "str":
                    block.append(game_field[m + n])
                elif mode == "col":
                    column = [game_field[i][m + n] for i in range(len(game_field))]
                    block.append(column)

            result.append(block)
            block = []

        game_field = result
        return True

    def mix_blocks():
        count = len(game_field)
        for i in range(count):
            n = random.randint(0, count - 1)
            block = game_field.pop(n)
            n = random.randint(0, count - 1)
            game_field.insert(n, block)

        return True

    def mix_strings_in_blocks():
        count = len(game_field)
        for i in range(count):
            for j in range(count):
                n = random.randint(0, count - 1)
                string = game_field[i].pop(n)
                n = random.randint(0, count - 1)
                game_field[i].insert(n, string)

        return True

    def create_strings_view():
        global game_field

        result = []
        count = len(game_field)

        for i in range(count):
            for j in range(count):
                result.append(game_field[i][j])

        game_field = result
        return True

    x = random.randint(1, 3)
    for i in range(x):
        create_blocks_view("col")
        mix_blocks()
        mix_strings_in_blocks()
        create_strings_view()
        
        create_blocks_view("str")
        mix_blocks()
        mix_strings_in_blocks()
        create_strings_view()


def hide_cells_in_game_field(difficulty_level):
    global game_field

    def count_zeros(field, string, column):
        in_string = 0
        in_column = 0
        in_square = 0

        for i in range(len(field)):
            if field[string][i] == 0:
                in_string += 1
            if field[i][column] == 0:
                in_column += 1

        square = detect_square(string, column)
        for i in range(3):
            for j in range(3):
                if field[i][j] == 0:
                    in_square += 1

        result = {"in_string": in_string, "in_column": in_column, "in_square": in_square}
        return result

    if difficulty_level == "easy":
        max_hide_cells = 20
    elif difficulty_level == "medium":
        max_hide_cells = 25
    elif difficulty_level == "hard":
        max_hide_cells = 30

    count_hide_cells = 0

    # будет заполнять по новой, пока не наберёт нужное число:
    while count_hide_cells != max_hide_cells:

        game_field_test = copy.deepcopy(game_field)
        count_hide_cells = 0
        new_zero = True # флаг защиты от зацикливания

        while count_hide_cells < max_hide_cells and new_zero:
            new_zero = False
            i = random.randint(0, len(game_field_test[0]) - 1)
            j = random.randint(0, len(game_field_test) - 1)

            if game_field_test[i][j] == 0:
                new_zero = True
                continue

            zeros = count_zeros(game_field_test, i, j)
            if zeros["in_string"] < 5 and zeros["in_column"] < 5 and zeros["in_square"] < 5:
                game_field_test[i][j] = 0
                count_hide_cells += 1
                new_zero = True

            # а тут всё просто, без условий)
            # game_field_test[i][j] = 0
            # count_hide_cells += 1
            # new_zero = True

    game_field = game_field_test
    print(count_hide_cells)


def solve_game_field():
    new_value = True # флаг защиты от зацикливания
    x = len(game_field[0])
    y = len(game_field)
    count_new_value = 0

    while new_value:
        new_value = False
        for i in range(x):
            for j in range(y):
                variants = list(create_unique_set(i, j))
                if len(variants) == 1:
                    game_field[i][j] = variants[0]
                    new_value = True
                    count_new_value += 1

    # иногда не может заполнить некоторые клетки, надо 
    # надо добавить другие методы решения, например
    # вставка случайного элемента из вариантов и далее
    # проверка всей матрицы (добавить функцию проверки!)
    # 
    print(count_new_value)


def main():
    fill_game_field()
    print_game_field()

    mix_game_field()
    print_game_field()

    hide_cells_in_game_field("hard")
    print_game_field()

    solve_game_field()
    print_game_field()


if __name__ == "__main__":
    main()

