#! /usr/bin/env python3

# File with alll utils functions for wordle 

# Open file named 'filename' and read its content 
def open_file_and_read(filename = None):
	
	word_list = list()
	file = open(filename, 'r')
	for row in file:
		word_list.append(row[:5])

	return word_list