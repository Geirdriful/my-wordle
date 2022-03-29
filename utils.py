#! /usr/bin/env python3
import requests
import json
from datetime import date

# File with alll utils functions for wordle 

''' Open file named 'filename' and read its content '''
def open_file_and_read(filename):
	
	word_list = list()
	file = open(filename, 'r')
	for row in file:
		word_list.append(row[:5])

	return word_list

''' Detection of green letters. Those letters exists on the WOTD and they are at the good place'''
def green_letters(list_wotd, list_player_word):

	list_return = list()

	for index in range(0,len(list_player_word)):
		if list_wotd[index] == list_player_word[index]:
			list_return.append(index)

	return list_return

''' Detection of orange letters. Those letters exists on the WOTD but they are not at the good place'''
def orange_letters(list_wotd, list_player_word):

	list_return = list()

	for index_wotd in range(0,len(list_wotd)):
		already_done = False
		for index_player_word in range(0, len(list_player_word)):
			if list_wotd[index_wotd] == list_player_word[index_player_word]:
				count_wotd = list_wotd.count(list_wotd[index_wotd])
				count_player_word = list_player_word.count(list_player_word[index_player_word])
			
				''' If list_player_word contains more than one occurence of the same letter whereas list_wotd not, then only one letter 
				are colored in orange
				If list_word contains more than one occurence of the same letter whereas list_player_word not, then only one letter 
				are colored in orange '''
				
				if count_player_word >= count_wotd and already_done == False:
					already_done = True
					list_return.append(index_player_word)
				elif count_player_word < count_wotd and already_done == False:
					list_return.append(index_player_word)
				
	return list_return

''' using dicolink API, fetch word of the day (based on date of today)
 https://api.dicolink.com/v1/mots/motdujour?date=2020-06-04&api_key=VOTRECLEFAPI '''
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

''' using dicolink API, fetch if the player word exists in the french dictionnary 
 https://api.dicolink.com/v1/mot/cheval/definitions?limite=200&api_key=VOTRECLEFAPI '''
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