
import random, copy


class GameField:
    def __init__(self, dim=3):
        self.dim = 3
        self.size = 9

        if self.is_valid_dimension(dim):
            self.dim = dim
            self.size = self.dim * self.dim

        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.fill()
        self.mix()
        self.hided_cells = {}


    # перенести в settings screen, а здесь уже просто получать значение при создании
    def is_valid_dimension(self, dim):
        valid_dimensions = [2, 3, 4, 5]

        if dim in valid_dimensions:
            return True
        else:
            print("Invalid dimension! Valid is:", valid_dimensions)
            print("Default value:", self.dim)
            return False


    def show(self):
        print("\n===========================\n")
        for i in self.matrix:
            print(i)
        print("\n===========================\n")


    def fill(self):
        def calc_value(value):
            if value > self.size:
                return value - self.size
            return value

        block_start = 1
        str_start = 1

        # по блокам:
        for i in range(0, self.size - 1, self.dim):
            str_start = block_start
            # по строкам:
            for j in range(i, i + self.dim):
                # по ячейкам:
                for n in range(0, self.size):
                    self.matrix[j][n] = calc_value(str_start + n)

                str_start += self.dim
            block_start += 1


    def mix(self):
        def transpose(): # not used
            list_of_columns = []
            # по столбцам:
            for j in range(len(self.matrix)):
                # берем j-тую ячейку каждой строки:
                column = [self.matrix[i][j] for i in range(len(self.matrix))]
                list_of_columns.append(column)
            
            return list_of_columns


        def mix_strings(): # not used
            mixed = []
            variants = list(range(len(self.matrix)))
            for i in range(len(self.matrix)):
                n = random.choice(variants)
                mixed.append(self.matrix[n])
                variants.remove(n)

            return mixed


        def create_blocks_view(mode):
            block = []
            result = []

            for n in range(0, self.size, self.dim):
                for m in range(self.dim):
                    if mode == "str":
                        block.append(self.matrix[m + n])
                    elif mode == "col":
                        column = [self.matrix[i][m + n] for i in range(len(self.matrix))]
                        block.append(column)

                result.append(block)
                block = []

            self.matrix = result
            return True


        def mix_blocks():
            count = len(self.matrix)
            for i in range(count):
                n = random.randint(0, count - 1)
                block = self.matrix.pop(n)
                n = random.randint(0, count - 1)
                self.matrix.insert(n, block)

            return True


        def mix_strings_in_blocks():
            count = len(self.matrix)
            for i in range(count):
                for j in range(count):
                    n = random.randint(0, count - 1)
                    string = self.matrix[i].pop(n)
                    n = random.randint(0, count - 1)
                    self.matrix[i].insert(n, string)

            return True


        def create_strings_view():
            result = []
            count = len(self.matrix)

            for i in range(count):
                for j in range(count):
                    result.append(self.matrix[i][j])

            self.matrix = result
            return True


        def change_digits_in_strings(times=3):
            for _ in range(times):
                digits = [i for i in range(1, len(self.matrix) + 1)]
                a = random.choice(digits)
                digits.remove(a)
                b = random.choice(digits)

                for string in self.matrix:
                    a_index = string.index(a)
                    b_index = string.index(b)
                    string[a_index] = b
                    string[b_index] = a


        # x = random.randint(1, 3)
        # for i in range(x):
        #     create_blocks_view("col")
        #     mix_blocks()
        #     mix_strings_in_blocks()
        #     create_strings_view()
        #     change_digits_in_strings()
            
        #     create_blocks_view("str")
        #     mix_blocks()
        #     mix_strings_in_blocks()
        #     create_strings_view()

        change_digits_in_strings(10)


    def hide_cells(self, hide_percent):
        if len(self.hided_cells) > 0:
            print("Already hided!")
            return

        if (hide_percent < 0) or (hide_percent > 100):
            print("Invalid value of 'hide_percent'(0-100)!")
            return

        max_hided_cells = round(((self.size * self.size) / 100) * hide_percent)
        self.hided_cells = {}

        while len(self.hided_cells) < max_hided_cells:
            y = random.randint(0, self.size - 1)
            x = random.randint(0, self.size - 1)

            if self.matrix[y][x] == 0:
                continue

            self.hided_cells[f"{y} {x}"] = {
                "matrix_coords": (y, x),
                "source_value": self.matrix[y][x],
                "input_value": 0,
                "screen_block": None,
            }

            self.matrix[y][x] = 0

        # print(len(self.hided_cells), self.hided_cells)


    # другой вариант, для более равномерного скрытия ячеек (экспериментальный)
    # не переделан для других размерностей!
    def hide_cells_2(self, difficulty_level):
        def count_zeros(field, string, column):
            in_string = 0
            in_column = 0
            in_square = 0

            for i in range(len(field)):
                if field[string][i] == 0:
                    in_string += 1
                if field[i][column] == 0:
                    in_column += 1

            square = self.detect_square(string, column)
            for i in range(self.dim):
                for j in range(self.dim):
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

            matrix_test = copy.deepcopy(self.matrix)
            count_hide_cells = 0
            new_zero = True # флаг защиты от зацикливания

            while count_hide_cells < max_hide_cells and new_zero:
                new_zero = False
                i = random.randint(0, len(matrix_test[0]) - 1)
                j = random.randint(0, len(matrix_test) - 1)

                if matrix_test[i][j] == 0:
                    new_zero = True
                    continue

                zeros = count_zeros(matrix_test, i, j)
                if zeros["in_string"] < 5 and zeros["in_column"] < 5 and zeros["in_square"] < 5:
                    matrix_test[i][j] = 0
                    count_hide_cells += 1
                    new_zero = True

                # а тут всё просто, без условий)
                # matrix_test[i][j] = 0
                # count_hide_cells += 1
                # new_zero = True

        self.matrix = matrix_test
        print("count_hide_cells:", count_hide_cells)


    def detect_square(self, string, column):
        def detect_borders(value):
            b1 = b2 = None
            start = 0
            end = self.dim - 1
            for _ in range(self.dim):
                if value >= start and value <= end:
                    b1 = start
                    b2 = end
                    break
                start += self.dim
                end += self.dim
            return (b1, b2)

        y1, y2 = detect_borders(string)
        x1, x2 = detect_borders(column)

        return (x1, y1, x2, y2)


    def solve(self):
        new_value = True # флаг защиты от зацикливания
        x = len(self.matrix[0])
        y = len(self.matrix)
        count_new_value = 0

        while new_value:
            new_value = False
            for i in range(x):
                for j in range(y):
                    variants = list(self.create_unique_set(i, j))
                    if len(variants) == 1:
                        self.matrix[i][j] = variants[0]
                        new_value = True
                        count_new_value += 1

        # иногда не может заполнить некоторые клетки, надо 
        # надо добавить другие методы решения, например
        # вставка случайного элемента из вариантов и далее
        # проверка всей матрицы (добавить функцию проверки!)
        # 
        print("count_new_value:", count_new_value)


    def create_unique_set(self, string, column):
        if self.matrix[string][column] != 0:
            return set()

        all_numbers = set(range(1, 10))
        exist_numbers = set()

        our_square = self.detect_square(string, column)
        x1 = our_square[0]
        y1 = our_square[1]
        x2 = our_square[2] + 1
        y2 = our_square[3] + 1

        for i in range(self.size):
            x = self.matrix[string][i]
            if x != 0:
                exist_numbers.add(x)

            y = self.matrix[i][column]
            if y != 0:
                exist_numbers.add(y)

        for i in range(y1, y2):
            for j in range(x1, x2):
                n = self.matrix[i][j]
                if n != 0:
                    exist_numbers.add(n)

        unique_set = all_numbers - exist_numbers

        # return all_numbers, exist_numbers, unique_set
        return unique_set


    def is_solved(self):
        for cell in self.hided_cells:
            if self.hided_cells[cell]["input_value"] != self.hided_cells[cell]["source_value"]:
                return False
        return True

