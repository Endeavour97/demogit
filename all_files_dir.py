#!/usr/bin/python3

import os

path = input('Enter the path where you want to get all the files and directories: ')
if os.path.exists(path):
	dirs = list(os.walk(path))[0][1]
	files = list(os.walk(path))[0][2]
	print('\nThe directories in the given path are:\n')
	for i in dirs:
		print(i)
	print('\nThe files in the given path are:\n')
	for j in files:
		print(j)
else:
	print('\nThe path does not exist')

