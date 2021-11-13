from everything.console_game_engine.game import Game
from everything.console import Colors

def run_demo1():

	def get_board():
		return [
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	[f'{Colors.RED}-','-','-','-','-','-','-','-','-','-',f'-{Colors.ENDC}'],
	['-','-','-','-','-','-','-','-','-','-','-'],
	['-','-','-','-','-','-','-','-','-','-','-']
	]

	def reset():
		demo1board.board = get_board()
		demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [0, 1], on_gem_collect)
		demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [1, 7], on_gem_collect)
		demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [4, 0], on_gem_collect)
		demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [6, 3], on_gem_collect)

		demo1.Collectible('@', [7, 10], on_portal)




	demo1 = Game()

	demo1board = demo1.Board(get_board())



	demo1player = demo1.Player('*', [0, 0], 0, 'top', 'You died!', 3 )



	def on_gem_collect(): #fix, late reaction
		demo1player.score+=1

	def on_portal():
		demo1.quit(True, "print('Congrats! You won!')")

	demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [0, 1], on_gem_collect)
	demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [1, 7], on_gem_collect)
	demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [4, 0], on_gem_collect)
	demo1.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [6, 3], on_gem_collect)

	demo1.Collectible('@', [7, 10], on_portal)

	def on_key(key):
		if key == 'r':
			demo1player.pos = [0,0]
			demo1player.score = 0
			reset()
		if key == 'e':
			demo1.quit()

	def fixed_update():
		if demo1player.pos[0] >= 8:
			demo1player.pos = [0, 0]
			demo1player.score = 0
			demo1player.die()
			reset()






	demo1.run(on_key, fixed_update)