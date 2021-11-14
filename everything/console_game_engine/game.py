import os
import time as t
import sys
from select import select
from everything.customexceptions import duplicatePlayerException, duplicateBoardException
from everything.console import Console
try:
	import getch
except ImportError:
	import mscvrt as getch

__all__ = ["Game"]
	
class Game():

	def __init__(self):
		self.player = None
		self.board_created = False
		self.player_created = False
		self.frames = 0
		self.board_created = False
		self.Entities = []
		self.Removed_Entities = []

	def get_key(self):
		first_char = getch.getch()
		if first_char == '\x1b':
			return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch.getch() + getch.getch()]
		else:
				return first_char

	def quit(self, clear, action, local_variables=None):
		self.active = False
		self.clear = clear
		self.quitaction = action
		self.quitaction_locals = local_variables
			

	def run(self, on_key=None, update=None): #refactor so the game grabs the player object from self.Player.{property} instead of passing in parameters through Game.run() ------ fixedupdate must be fixed, is currently only called after a keypress
		self.active = True
		while self.active:
			dr,dw,de = select([sys.stdin], [], [], 0)
			
			Console.clear()

			try:
				update()
			except NameError:
				pass
			except TypeError:
				pass
			
			board = self.board.board
			player = self.player.player
			pos = self.player.pos

			if self.player.is_dead:
				print(self.player.death_message)
				self.player.is_dead = False
				t.sleep(self.player.death_message_hold)

			for Entity in self.Entities:
				if pos == Entity[0] and Entity[1] and Entity[2]:
					Entity[3]()
					self.Entities.remove(Entity)
					self.Removed_Entities.append(Entity)

			for Entity in self.Entities:
				board[Entity[0][0]][Entity[0][1]] = Entity[1]

			if self.player.shown:
				board[pos[0]][pos[1]] = player

			if self.player.score != None and self.player.score_pos == 'top':
				print(f'Score: {self.player.score}')
				

			for i in range(0,len(board)):
				for j in range(0, len(board[i])):
					if board[i][j] == player:
						if i == pos[0] and j  == pos[1]:
							pass
						else:
							if self.board.replacechar is None:
								board[i][j] = self.board.get_default_board()[i][j]
							else:
								board[i][j] = self.board.replacechar

			for i in range(0, len(board)):
				for j in range(0, len(board[i])):
					print(board[i][j], end = ' ')
				print()

			if not self.active:
				break

			if self.player.score != None and self.player.score_pos == 'bottom':
				print(f'Score: {self.player.score}')


			if self.player.arrow_keys:
				move = self.get_key()
			else:
				move = getch.getch()
			try:
				on_key(move)
			except NameError:
				pass
			except TypeError:
				pass



			


		
			
			if not self.player.wasd:
				if move == 'up':
					pos[0] -= 1
					if pos[0] < 0:
						pos[0]+=1

				elif move == 'down':
					pos[0] += 1
					if pos[0] > self.board.rows-1:
						pos[0]-=1

				elif move == 'right':
					pos[1] += 1
					if pos[1] > self.board.columns-1:
						pos[1]-=1

				elif move == 'left':
					pos[1] -= 1
					if pos[1] < 0:
						pos[1]+=1
				
			else:
				if move == 'up' or move == 'w':
					pos[0] -= 1
					if pos[0] < 0:
						pos[0]+=1

				elif move == 'down' or move == 's':
					pos[0] += 1
					if pos[0] > self.board.rows-1:
						pos[0]-=1

				elif move == 'right' or move == 'd':
					pos[1] += 1
					if pos[1] > self.board.columns-1:
						pos[1]-=1

				elif move == 'left' or move == 'a':
					pos[1] -= 1
					if pos[1] < 0:
						pos[1]+=1
			
			self.frames+=1

		if self.clear:
			Console.clear()	

		try:
			self.quitaction()
		except TypeError:
			try:
				exec(self.quitaction, self.quitaction_locals)
			except Exception as e:
				print(f'Could not perform quitaction: {e}')
														

	def Player(self, player_character, pos, score, score_pos, death_message, death_message_hold_time, arrowkeys=True, wasd=True, collideaction=None):
		if self.player_created:
			raise duplicatePlayerException(self.player)
		else:
			self.player_created = True
			info = _Player(player_character, pos, score, score_pos, death_message, death_message_hold_time, arrowkeys=True, wasd=True, collideaction=None)
			self.Entities.append([info.pos, info.player, info.state, info.collideaction])
			self.player = info
			return info

	def Entity(self, character, position, collideable=False, collideaction=None):
		info = _Entity(character, position, collideable, collideaction)
		self.Entities.append([info.pos, info.character, info.state, info.action])
		return info

	def Collectible(self, character, position, action):
		info = _Collectible(character, position, action)
		self.Entities.append([info.pos, info.character, info.state, info.action])
		return info

	
	def Board(self, gameboard):
		if self.board_created:
			raise duplicateBoardException(self.board)
		else:
			self.board_created = True
			info = _Board(gameboard)
			self.board = info
			return info

		

class _Player():
	def __init__(self, player_character, pos, score, score_pos, death_message, death_message_hold_time, arrowkeys=True, wasd=True, collideaction=None):
		self.player = player_character
		self.pos = pos
		self.arrow_keys = arrowkeys
		self.wasd = wasd
		self.shown = True
		self.score = score
		self.score_pos = score_pos
		self.is_dead = False
		self.state = False
		self.death_message = death_message
		self.death_message_hold = death_message_hold_time
		self.collideaction = collideaction

	def hide(self):
		self.shown = False

	def show(self):
		self.shown = True

	def die(self):
		self.is_dead = True

class _Collectible():
	def __init__(self, collectible_character, position, action):
		self.character = collectible_character
		self.pos = position
		self.state = True
		self.action = action


class _Entity():
	def __init__(self, character, position, collideable, collideaction):
		self.character = character
		self.pos = position
		self.collideable = collideable
		if self.collideable:
			self.state = 'collide'
		else:
			self.state = False
		self.action = collideaction

class _Board():
	def __init__(self, gameboard):
		self.board = gameboard
		self.replacechar = None
		self.columns = len(gameboard[0])
		self.rows = len(gameboard)
		self.boardstring = ''
		for i in range(0, self.rows):
			for j in range(0, self.columns):
				self.boardstring+=self.board[i][j]
	
	def get_default_board(self):
		gameboard = []
		index = 0
		for i in range(0, self.rows):
			gameboard.append([])
			for j in range(0, self.columns):
				gameboard[i].append(self.boardstring[index:index+1])
				index+=1

		return gameboard

	def always_replace_with(self, char):
		self.replacechar = char
	
	def replace_char(self, pos, char):
		pos = pos[1]*(self.columns-1)
		pos+=pos[2]
		str1 = self.boardstring[pos-1]
		str2 = self.boardstring[-pos]
		str1+=char
		self.boardstring = str1+str2

	
