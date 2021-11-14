import sys
import asyncio
import time
import os
import tkinter
import random
import math
import datetime
import contextlib
try:
	from pytube import YouTube
	import pygame
except ImportError:
	os.system('pip install pytube')
	os.system('pip install pygame')
	from pytube import YouTube
	import pygame

'''

DISCLAIMER: THE FUNCTIONS AND MODULES IN THIS LIBRARY WERE NOT CREATED BY THE AUTHOR OF THIS LIBRARY. THEY ARE SIMPLY ADAPTATIONS FOR EASIER USE.

Welcome to the everything library! This library utilizes other modules such as:
-time
-os
-math
-pygame
-pytube

The library uses these to adapt them and make them easier to use. This is a huge library, so importing the whole thing is probably unneccessary and will slow the program down. This library includes a lot of modules and you can import most things you need from here.

Here we have the start of the classes, used to separate the different methods available in the library. Each of the parent classes are labeled and the groups of the static and non-static methods are also labeled.

The classes here contain modules related to each other so you can import them all at once instead of one by one.

'''

'''Pyinter (Pygame)'''

pyicon = pygame.image.load('python.png')

class pyinter():
	class display():
		size = (0,0)
		title = 'Pyinter Window'
		icon = pyicon
		def displaysetsstats(size, title, icon):
			size = size
			title = title
			icon = icon

		stats = {
				'size' : size,
				'title' : title,
				'icon' : icon
			}

	def init():
		pygame.init()
	
	def create_display(size, title = None, icon = None):
		try:
			pyinter.display.displaysetsstats(size, title, icon)
			interfaceScreen = pygame.display.set_mode(size)
			if title == None:
				title = 'Pyinter Window'
				interfaceScreen = pygame.display.set_caption(title)
			else:
				interfaceScreen = pygame.display.set_caption(title)
			if icon == None:
				icon = pyicon
				pygame.display.set_icon(icon)
			else:
				pygame.display.set_icon(icon)
		except Exception as e:
			print(e)
	
	def create_font():
		pass	