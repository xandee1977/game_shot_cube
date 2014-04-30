#! /usr/bin/env python
from random import randint

class box_groups:
	 # Ammount of boxes per line
	box_ammount = 10
	
	# Colors of boxes	
	box_colors = [
		(255,0,0),
		(0,0,255),
		(0,255,0)
	]

	# List of boxes lines
	box_lines = []

	def __init__ (self):
		print("Loading box_groups ...")

	# Getting a line sorting box colors
	def get_line(self):
		result = []
		for i in range(self.box_ammount):
			item = {
				"color" : randint(0, (len(self.box_colors)-1)), # Index of desired color
				"show" : 1, # Control the box visibility
				"rect": None
			}
			result.append(item)
		return result

	"""
	# Getting an item by rect
	def get_item(self, rect):
		for line in self.box_lines:
			for item in line:
	"""

	# Append itens to box_line list
	def feed_box_lines(self):
		self.box_lines.append(self.get_line())

	# Getting the box lines
	def get_box_lines(self):
		return self.box_lines

	def get_color(self, index):
		return self.box_colors[index]
