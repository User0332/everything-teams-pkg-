from everything.console_game_engine.game import Game
from everything.console import Console
from everything.console import Colors

def run_demo1():

	def getboard():
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
	8



	mygame = Game()

	mygameboard = mygame.Board(getboard(), '-')



	myplayer = mygame.Player('*', [0, 0], 0, 'top', 'You died!', 3 )



	def on_gem_collect(): #fix, late reaction
		myplayer.score+=1

	def on_portal():
		mygame.quit(True, "print('Congrats! You won!')")

	gem1 = mygame.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [0, 1], on_gem_collect)
	gem2 = mygame.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [1, 7], on_gem_collect)
	gem3 = mygame.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [4, 0], on_gem_collect)
	gem4 = mygame.Collectible(f'{Colors.GREEN}0{Colors.ENDC}', [6, 3], on_gem_collect)

	my_entity = mygame.Entity('O', [3, 3])



	portal = mygame.Collectible('@', [7, 10], on_portal)

	def on_key(key):
		if key == 'r':
			myplayer.pos = [0,0]
			myplayer.score = 0
			mygame.Board.board = getboard()
		if key == 'e':
			mygame.quit()

	def on_player_move():
		pass


	def fixed_update():
		if myplayer.pos[0] >= 7:
			myplayer.pos = [0, 0]
			myplayer.score = 0
			myplayer.die()






	mygame.run(on_key, fixed_update)