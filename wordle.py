#! /usr/bin/env python3
import random

def open_file_and_read():
	
	word_list = list()
	file = open('mots.txt', 'r')
	for row in file:
		word_list.append(row[:5])
	return word_list

def main():

	word_list = open_file_and_read()

	number = random.randint(0, len(word_list))
	print(word_list[number])

if __name__ == '__main__':
	main()