#! /usr/bin/env python3
import utils
import service_api
from gestion_exception import HTTPException
import random
import sys

def main():

	''' Déclaration variables '''
	list_lettres_unique = list()
	list_letter_of_the_day = list()
	
	word_player = ""
	attempt = 0

	service = service_api.ServiceAPI()

	''' Selection d'un mot parmi la liste '''
	try:
		word_of_the_day = service.get_word_of_the_day(service.api_key)
	except KeyError:
		sys.exit('Selection du mot impaaaawsible')
	except HTTPException as httpException:
		# import pdb
		# pdb.set_trace()
		print(httpException.args[0])

		sys.exit("Fin du programme. Attendez quelques minutes avant de relancer svp.\n")
	
	print("Selection d'un mot de " + str(len(word_of_the_day)) + " lettres ...")
	list_letter_of_the_day = [char for char in word_of_the_day]
	
	''' tant que le joueur n'a pas trouvé et qu'il n'a pas fait 6 tentatives '''
	while word_player.upper() != word_of_the_day and attempt < 6 :
		''' Entrée clavier par le joueur '''
		try:
			word_player = input("\nProposition ? ")
		except KeyboardInterrupt:
			sys.exit(' Interruption clavier')
		
		try:
			player_word_exists = service.is_valid(word_player)
		except ValueError:
			sys.exit('Un ou plusieurs caractere(s) inconnus')
		except HTTPException as httpException:
		# import pdb
		# pdb.set_trace()
			print(httpException.args[0])
			sys.exit("Fin du programme. Attendez quelques minutes avant de relancer svp.\n")

		while player_word_exists == False or len(word_of_the_day) != len(word_player):
			if player_word_exists == False:
				print("le mot '", word_player,"' n'est pas un mot valide")
			else:
				print('Merci de faire une proposition de',str(len(word_of_the_day)),'lettres')
			try:
				word_player = input("\nProposition ? ")
			except KeyboardInterrupt:
				sys.exit('Interruption clavier')

			try:
				player_word_exists = service.is_valid(word_player)
			except KeyError:
				sys.exit('Erreur lors de la recherche du mot')
			except HTTPException as httpException:
				# import pdb
				# pdb.set_trace()
				print(httpException.args[0])
				sys.exit("Fin du programme. Attendez quelques minutes avant de relancer svp.\n")

		
		''' Si ce n'est pas le mot du jour, il faut chercher les lettres oranges/vertes'''
		if not utils.find_word_of_the_day(word_player, word_of_the_day):
				
			''' Detection of green letters '''
			return_green = utils.green_letters(word_of_the_day, word_player.upper())

			''' Detection of orange letters '''

			return_orange = utils.orange_letters(word_of_the_day,word_player.upper())

			''' Affichage '''
			for l in range(0, len(word_player)):
				if l in return_green:
					print("\033[0;32;40m" + word_player[l].upper() + "\033[0m", end ='')
				elif l in return_orange:
					print("\033[0;33;40m" + word_player[l].upper() + "\033[0m", end ='')
				else:
					print("" + word_player[l].upper(), end = '')
			attempt = attempt + 1
		else:
			print("\033[0;32;40m" + word_of_the_day + "\033[0m")
			sys.exit("Bravo")
	
	''' Fin de partie '''
	if attempt == 6:
		print("\nDommage, vous avez perdu. Le mot a trouver été :", word_of_the_day)

if __name__ == '__main__':
	main()