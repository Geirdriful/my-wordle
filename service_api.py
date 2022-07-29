#! /usr/bin/env python3
import utils
import requests
from datetime import date

class ServiceAPI(object):

	# def __init__(self):
	# 	self.session = requests.Session()
	
	# def close(self):
	# 	self.session.close()

	# def __exit__(self, exc_type, exc_value, traceback):
	# 	self.close()

	# def open(self):
	# 	self.session = requests.Session



	''' Recupere le mot du jour en utilisant sur l'api de dicolink (En se basant sur la date du jour)'''
	def get_word_of_the_day(self):

		today = date.today()
		header = {
			'Content-Type': 'application/json'
		}
		url = "https://api.dicolink.com/v1/mots/motdujour?date="+str(today)+"&api_key=ANvGBoV1-G7Ioi4SIix_dXPzV1y1gCDD"

		with requests.Session() as session:
			response = session.get(url, headers=header)
			status_code = response.status_code

			if status_code == 200:
				print(response.json()['mot'].upper(),len("sedition"))
				return response.json()['mot'].upper()
			else:
				print('error in request', status_code, response_json)

	''' Trouve si le mot du joueur existe dans le dictionnaire francais. Si oui, le mot est valide, si non il est invalide 
		Utilise l'api de dicolink '''
	def is_valid(self, word):

		header = {
			'Content-Type': 'application/json'
		}
		url = "https://api.dicolink.com/v1/mot/"+ str(word) +"/definitions?limite=200&api_key=ANvGBoV1-G7Ioi4SIix_dXPzV1y1gCDD"

		with requests.Session() as session:
			response = session.get(url, headers=header)
			status_code = response.status_code

			if status_code == 200:
				if isinstance(response.json(), dict) and response.json().get('error'):
					return False
				return True
			else:
				raise Exception("Error in request", status_code, response_json)
				# print('error in request', status_code, response_json)
