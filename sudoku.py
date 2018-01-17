
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


	for n in game_field:
		print(n)

fill_game_field()
print('\n===========\n')

def mix_game_field():

	def transpose():
		list_of_columns = []
		# по столбцам:
		for j in range(len(game_field)):
			# берем j-тую ячейку каждой строки:
			column = [game_field[i][j] for i in range(len(game_field))]
			list_of_columns.append(column)
		
		return list_of_columns


	result = transpose()
	for n in result:
		print(n)

mix_game_field()