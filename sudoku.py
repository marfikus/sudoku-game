
import random

# game_field = [
# [1, 2, 3, 2, 0, 0, 5, 0, 0],
# [4, 5, 6, 0, 0, 0, 0, 0, 0],
# [7, 8, 9, 0, 0, 0, 0, 0, 0],
# [4, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 3, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0, 5, 0]]

game_field = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_game_field():
	print('\n===========================\n')

	for i in game_field:
		print(i)

	print('\n===========================\n')

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

	def transpose():
		list_of_columns = []
		# по столбцам:
		for j in range(len(game_field)):
			# берем j-тую ячейку каждой строки:
			column = [game_field[i][j] for i in range(len(game_field))]
			list_of_columns.append(column)
		
		return list_of_columns # not used

	def mix_strings():
		mixed = []
		variants = list(range(len(game_field)))
		for i in range(len(game_field)):
			n = random.choice(variants)
			mixed.append(game_field[n])
			variants.remove(n)

		return mixed # not used

	def create_blocks_view(mode):
		global game_field

		block = []
		result = []

		for n in range(0, 9, 3):
			for m in range(3):
				if mode == 'str':
					block.append(game_field[m + n])
				elif mode == 'col':
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

	create_blocks_view('str')
	print_game_field()
	mix_blocks()
	print_game_field()
	mix_strings_in_blocks()
	print_game_field()
	create_strings_view()
	# print_game_field()

	# x = random.randint(3, 5)
	# for i in range(x):
	# 	game_field = transpose()
	# 	game_field = mix_strings()

def hide_cells_in_game_field(difficulty_level):

	def count_zeros(string, column):
		in_string = 0
		in_column = 0
		in_square = 0

		for i in range(len(game_field)):
			if game_field[string][i] == 0:
				in_string += 1
			if game_field[i][column] == 0:
				in_column += 1

		square = detect_square(string, column)
		for i in range(3):
			for j in range(3):
				if game_field[i][j] == 0:
					in_square += 1

		result = {'in_string': in_string, 'in_column': in_column, 'in_square': in_square}
		return result

	# print(count_zeros(0, 0))

	if difficulty_level == 'easy':
		max_hide_cells = 20
	elif difficulty_level == 'medium':
		max_hide_cells = 25
	elif difficulty_level == 'hard':
		max_hide_cells = 30

	count_hide_cells = 0
	new_zero = True	# флаг защиты от зацикливания

	while count_hide_cells < max_hide_cells and new_zero:
		new_zero = False
		i = random.randint(0, len(game_field[0]) - 1)
		j = random.randint(0, len(game_field) - 1)

		if game_field[i][j] == 0:
			new_zero = True
			continue

		# этот вариант надо додумать, тк при таком условии иногда не набирает и 20,
		# хотя, может и норм 
		zeros = count_zeros(i, j)
		if zeros['in_string'] < 5 and zeros['in_column'] < 5 and zeros['in_square'] < 5:
			game_field[i][j] = 0
			count_hide_cells += 1
			new_zero = True

		# а тут всё просто, без условий)
		# game_field[i][j] = 0
		# count_hide_cells += 1
		# new_zero = True

	print(count_hide_cells)


fill_game_field()
print_game_field()

# mix_game_field()
# print_game_field()


# game_field[0][0] = 0
# game_field[0][5] = 0
# game_field[4][7] = 0
# game_field[8][8] = 0

# print_game_field()

hide_cells_in_game_field('hard')

print_game_field()

# print(create_unique_set(0, 0))
# print(create_unique_set(0, 5))
# print(create_unique_set(4, 7))
# print(create_unique_set(8, 8))

for i in range(9):
	for j in range(9):
		print(i, j, create_unique_set(i, j))

