#not /usr/bin/env python
# -*- coding: utf-8 -*-

# Peter Fajner 2015
# peterfajner@gmail.com
# github.com/PeterFajner

# A simple game of flipping squares

import random

def main():
	matrix = generate_matrix()
	done = False
	num_moves = 0
	randomize(matrix)
	refresh_screen(matrix, num_moves)
	while not done:
		num_moves += 1
		reverse(matrix, get_input(matrix))
		refresh_screen(matrix, num_moves)
		win = check_win(matrix)
		if win:
			print "You won in %d moves!" % num_moves
			done = True

def generate_matrix():
	valid = False
	x,y = 0,0
	while not valid:
		xy = raw_input("Enter dimensions (sample: 3 3): ")
		xy = xy.split(" ")
		try:
			x = int(xy[0])
			y = int(xy[1])
		except (ValueError, IndexError):
			print "Incorrect notation!"
			continue
		if x > 0 and y > 0:
			valid = True
		else:
			print "Must be positive!"
	matrix = []
	for i in xrange(0, y):
		matrix.append([])
		for j in xrange(0, x):
			matrix[i].append(False)
	return matrix

def randomize(matrix):
	for i in xrange(0, len(matrix)):
		for j in xrange(0, len(matrix[i])):
			matrix[i][j] = random.choice([True, False])

def get_input(matrix): # matrix input for checking validity
	valid = False
	x,y=-1,-1
	while not valid:
		in_ = raw_input("x y: ")
		in_ = in_.split(" ")
		if len(in_) != 2:
			print "Enter two coordinates!"
			continue
		x = int(in_[0])
		y = int(in_[1])
		if (x < 0 or y < 0 or x > (len(matrix[0]) - 1) or y > (len(matrix) - 1)):
			print "Out of bounds!"
		else:
			valid = True
	return [x,y]

def refresh_screen(matrix, num_moves):
	print "Move " + str(num_moves);
	print ""
	for row in matrix:
		for column in row:
			value = u"□"
			if column:
				value = u"■"
			print(value + " "),
		print ""

def check_win(matrix):
	for row in matrix:
		for column in row:
			if not column:
				return False
	return True

def reverse(matrix, pos): #pos is [x,y]
	x,y = pos[0],pos[1]
	matrix[y][x] = not matrix[y][x]
	if x > 0:
		matrix[y][x-1] = not matrix[y][x-1]
	if x < len(matrix[0]) - 1:
		matrix[y][x+1] = not matrix[y][x+1]
	if y > 0:
		matrix[y-1][x] = not matrix[y-1][x]
	if y < len(matrix) - 1:
		matrix[y+1][x] = not matrix[y+1][x]

main()