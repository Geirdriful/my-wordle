#! /usr/bin/env python3
import requests
import json
from datetime import date

# File with alll utils functions for wordle 

''' Ouvre le fichier 'filename' et lis son contenu '''
def open_file_and_read(filename):
	
	word_list = list()
	file = open(filename, 'r')
	for row in file:
		word_list.append(row[:5])

	return word_list

''' Detection des lettres vertes. Ces lettres sont presentes dans le WOTD et sont a la bonne place'''
def green_letters(list_wotd, list_player_word):

	list_return = list()

	for index in range(0,len(list_player_word)):
		if list_wotd[index] == list_player_word[index]:
			list_return.append(index)

	return list_return

''' Detection des lettres oranges. Ces lettres sont presente dans le WOTD mais ne sont pas a la bonne place'''
def orange_letters(list_wotd, list_player_word):

	list_return = list()

	for index_wotd in range(0,len(list_wotd)):
		already_done = False
		for index_player_word in range(0, len(list_player_word)):
			if list_wotd[index_wotd] == list_player_word[index_player_word]:
				count_wotd = list_wotd.count(list_wotd[index_wotd])
				count_player_word = list_player_word.count(list_player_word[index_player_word])
			
				''' Si list_player_word contient plus qu'une occurence de la meme lettre alors que list_wotd non, alors seulement une seule lettre
				est affichee en orange
				Si list_wotd contient plus d'une occurrence de la meme lettre tandis que list_player_word non, alors seulement une seule
				lettre est affichee en orange'''
				
				if count_player_word >= count_wotd and already_done == False:
					already_done = True
					list_return.append(index_player_word)
				elif count_player_word < count_wotd and already_done == False:
					list_return.append(index_player_word)
				
	return list_return

''' Recupere le mot du jour en utilisant sur l'api de dicolink (En se basant sur la date du jour)'''
def get_word_of_the_day():

	today = date.today()
	header = {
		'Content-Type': 'application/json'
	}
	url = "https://api.dicolink.com/v1/mots/motdujour?date="+str(today)+"&api_key=ANvGBoV1-G7Ioi4SIix_dXPzV1y1gCDD"

	response = requests.get(url, headers=header)
	response_json = json.loads(response.text)

	print(response_json['mot'])
	return response_json['mot'].upper()

''' Trouve si le mot du joueur existe dans le dictionnaire francais. Si oui, le mot est valide, si non il est invalide 
	Utilise l'api de dicolink '''
def search_player_word(word):
	
	header = {
		'Content-Type': 'application/json'
	}
	url = "https://api.dicolink.com/v1/mot/"+ str(word) +"/definitions?limite=200&api_key=ANvGBoV1-G7Ioi4SIix_dXPzV1y1gCDD"

	response = requests.get(url, headers=header)
	response_json = json.loads(response.text)

	if len(response_json) != 1:
		return 200
	else:
		return 400
	
	print(response_json)