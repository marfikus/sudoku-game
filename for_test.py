
import sudoku

while True:
	x = input(':')
	if x == 'q':
		break

	x = list(x.split())

	print(sudoku.detect_square(x[0], x[1]))