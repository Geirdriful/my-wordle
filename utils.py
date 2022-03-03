#! /usr/bin/env python3

# File with alll utils functions for wordle 

''' Open file named 'filename' and read its content '''
def open_file_and_read(filename = None):
	
	word_list = list()
	file = open(filename, 'r')
	for row in file:
		word_list.append(row[:5])

	return word_list

''' Returns the indexes of all occurrences of give element in
	the list- listOfElements '''
def get_index_positions(list_of_elems, element):
	
	index_pos_list = []
	index_pos = 0
	while True:
		try:
			''' Search for item in list from indexPos to the end of list '''
			index_pos = list_of_elems.index(element, index_pos)
			''' Add the index position in list '''
			index_pos_list.append(index_pos)
			index_pos += 1
		except ValueError as e:
			break
	return index_pos_list

''' Detection of green letters. Those letters exists on the WOTD and they are at the good place'''
def green_letters(list_wotd = None, list_player_word = None):

	list_return = list()

	for index in range(0,len(list_player_word)):
		if list_wotd[index] == list_player_word[index]:
			list_return.append(index)

	return list_return

''' Detection of orange letters. Those letters exists on the WOTD but they are not at the good place'''
def orange_letters(list_wotd = None, list_player_word = None):

	list_return = list()

	for index_wotd in range(0,len(list_wotd)):
		already_done = False
		for index_player_word in range(0, len(list_player_word)):
			if list_wotd[index_wotd] == list_player_word[index_player_word]:
				count_wotd = list_wotd.count(list_wotd[index_wotd])
				count_player_word = list_player_word.count(list_player_word[index_player_word])
			
				''' Si list_player_word plusieurs fois la même lettre alors que list_wotd non, il ne faut mettre en orange 
				qu'une seule occurence de la lettre 
				
				Si list_wotd plusieurs fois la même lettre alors que list_player_word non, il ne faut mettre en orange 
				la lettre'''
				if count_player_word >= count_wotd and already_done == False:
					already_done = True
					list_return.append(index_player_word)
				elif count_player_word < count_wotd and already_done == False:
					list_return.append(index_player_word)
				
	return list_return