board_size = 3
# игровое поле
board = [1,2,3,4,5,6,7,8,9]




def draw_board():
	print (('_' * 4 * board_size ))
	for i in range(board_size):
		print ((' ' * 3 + '|') * 3)
		print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
		print (('_' * 3 + '|') * 3)

def check_win(board):
	win = False

	win_comb = (
		(0,1,2), (3,4,5), (6,7,8),	# горизонтальные линии
		(0,3,6), (1,4,7), (2,5,8),	# вертикальные линии
		(0,4,8), (2,4,6) 			# диагональные линии
	)

	for pos in win_comb:
		if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','O')):
			win = board[pos[0]]

	return win

def game_step(index, char):
	if (index > 10 or index < 1 or board[index-1] in ('X','O')):
		return False

	board[index-1] = char
	return True
def PC_step(human, ai):
	available_steps = [i-1 for i in board if type(i) == int]
	win_steps = (4, 0, 6, 8, 1, 3, 5, 7)

	for char in (ai, human):
		for pos in available_steps:
			board_ai = board[:]
			board_ai[pos] = ai
			if (check_win(board_ai) != False):
				return pos

	for pos in win_steps:
		if (pos in available_steps):
			return pos

	return False

def next_player(player):

	if(player == 'X'):
		return 'O'

	return 'X'
def start_game(mode):
	player = 'X'
	ai_player = 'O'
	step = 1

	draw_board()

	while (step < 9) and (check_win(board) == False):
		index = input('Ходит ' + player + '. Введите номер поля (0 - выход):')

		if (int(index) == 0):
			break

		if (game_step(int(index), player)):
			print('Удачный ход')

			player = next_player(player)

			step += 1
			if (mode == '2'):
				ai_step = PC_step('X', 'O')
				if (type(ai_step) == int):
					board[ai_step] = ai_player
					player = next_player(player)
					step += 1


			draw_board()
		else:
			print('Неверный номер! Повторите!')

	if (step == 10):
		print('Игра оконцена. Ничья!')

	elif check_win(board) != False:
		print('Выиграл ' + check_win(board))

print('Приветствую в игре!')

mode = 0
while mode not in ('1', '2'):

	mode =input("Режим игры:\n1 - Игрок против Игрока\n2 - Игрок против ИИ\nВыберите режим")
start_game(mode)

