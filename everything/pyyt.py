import os
from everything.console.console import Console
from pytube import YouTube


Console.clear()

class pyyt():
	@staticmethod
	def download(cls, link):
		try:
			yt = YouTube(link)
			yt.streams.get_highest_resolution().download()
		except Exception as e:
			print(e)
	@staticmethod
	def stats(cls, link):
		try:
			yt = YouTube(link)
			stats = {
							'title' : yt.title,
							'description' : yt.description,
							'views' : yt.views,
							'rating' : yt.rating
							 }
			return stats
		except Exception as e:
			print(e)
