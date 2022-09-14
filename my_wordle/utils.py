#! /usr/bin/env python3
import requests
import json
from datetime import date

''' Detection des lettres vertes. Ces lettres sont presentes dans le WOTD et sont a la bonne place'''
# def green_letters(list_wotd, list_player_word):

# 	list_return = list()

# 	for index in range(0,len(list_player_word)):
# 		if list_wotd[index] == list_player_word[index]:
# 			list_return.append(index)

# 	return list_return


def green_letters(wotd, player_word):

	list_return = list()
	for index_player_word, char_player_wotd in enumerate(player_word):
		if char_player_wotd in wotd and char_player_wotd == wotd[index_player_word]:
			list_return.append(index_player_word)

	return list_return

''' Detection des lettres oranges. Ces lettres sont presente dans le WOTD mais ne sont pas a la bonne place'''
def orange_letters(wotd, player_word):
	list_return = list()

	for index_player_word, char_player_wotd in enumerate(player_word):
		if char_player_wotd in wotd and char_player_wotd != wotd[index_player_word]:
			count_wotd = wotd.count(char_player_wotd)
			count_player_word = player_word.count(char_player_wotd)
			if count_player_word >= count_wotd and index_player_word == player_word.find(char_player_wotd):
				list_return.append(index_player_word)

	return list_return


	# for index_wotd, char_wotd in enumerate(wotd):
	# 	already_done = False
	# 	for index_player_word, char_player_wotd in  enumerate(player_word):
	# 		if char_wotd == char_player_wotd:
	# 			count_wotd = wotd.count(char_wotd)
	# 			count_player_word = player_word.count(char_player_wotd)
			
	# 			''' Si player_word contient plus qu'une occurence de la meme lettre alors que wotd non, alors seulement une seule lettre
	# 			est affichee en orange
	# 			Si wotd contient plus d'une occurrence de la meme lettre tandis que player_word non, alors seulement une seule
	# 			lettre est affichee en orange'''
				
	# 			if count_player_word >= count_wotd and already_done == False:
	# 				already_done = True
	# 				list_return.append(index_player_word)
	# 			elif count_player_word < count_wotd and already_done == False:
	# 				list_return.append(index_player_word)
				
	# return list_return

def find_word_of_the_day(word_player, word_of_the_day):
	if word_player.upper() == word_of_the_day:
		return True
	else:
		return False 