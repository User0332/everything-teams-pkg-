from everything.console_game_engine.game import Game
from everything.console import Colors


def run_demo2():
	demo2 = Game()

	gameboard = demo2.Board([['0','0','0','0','0'], ['0','0','0','0','0'], ['0','0','0','0','0'], ['0','0','0','0','0'], ['0','0','0','0','0']])

	player = demo2.Player('*', [0, 0], None, None, None, None)

	def update():
		print(f'{Colors.BOLD}Key presses: {demo2.frames} {Colors.ENDC}')
		print(f'Boardstring: {gameboard.boardstring}')

		if gameboard.board == [['1','1','1','1','1'], ['1','1','1','1','1'], ['1','1','1','1','1'], ['1','1','1','1','1'], ['1','1','1','1','1']]:
			demo2.quit(True, 'print("Congrats! You Won!")')	

		if gameboard.board[player.pos] == '1':
			gameboard.replace_char(player.pos, '0')
		else:
			gameboard.replace_char(player.pos, '1')

	demo2.run(update=update)