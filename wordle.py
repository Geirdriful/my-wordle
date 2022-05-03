#! /usr/bin/env python3
import utils
import random

def main():

	''' Déclaration variables '''
	list_lettres_unique = list()
	list_letter_of_the_day = list()
	
	word_player = ""
	attempt = 0

	''' Selection d'un mot parmi la liste '''
	word_of_the_day = utils.get_word_of_the_day()
	# word_list = utils.open_file_and_read('mots.txt')

	# number = random.randint(0, len(word_list))
	# word_of_the_day = word_list[number]
	
	print("Selection d'un mot de " + str(len(word_of_the_day)) + " lettres ...")
	list_letter_of_the_day = [char for char in word_of_the_day]
	# for index in range(0, len(word_of_the_day)):
	# 	list_letter_of_the_day.append(word_of_the_day[index])
	
	''' tant que le joueur n'a pas trouvé et qu'il n'a pas fait 6 tentatives '''
	while word_player.upper() != word_of_the_day and attempt < 6 :
		''' Entrée clavier par le joueur '''
		word_player = input("\nProposition ? ")
		
		player_word_exists = utils.search_player_word(word_player)
		while player_word_exists == 400 or len(word_of_the_day) != len(word_player):
			if player_word_exists == 400:
				print("le mot '", word_player,"' n'est pas un mot valide")
			else:
				print('Merci de faire une proposition de',str(len(word_of_the_day)),'lettres')
			word_player = input("\nProposition ? ")
			player_word_exists = utils.search_player_word(word_player)

		
		''' Si ce n'est pas le mot du jour, il faut chercher les lettres oranges/vertes'''
		if not utils.find_word_of_the_day(word_player, word_of_the_day):
			''' Découpage du mot du joueur et ajout dans une liste '''
			list_letter_of_the_player = list()
			for index in range(0, len(word_of_the_day)):
				list_letter_of_the_player.append(word_player[index].upper())
				

			''' Detection of green letters '''
			return_green = utils.green_letters(list_letter_of_the_day, list_letter_of_the_player)

			''' Detection of orange letters '''
			list_wotd_tmp = list_letter_of_the_day.copy()
			list_player_tmp = list_letter_of_the_player.copy()

			if return_green:
				for i in return_green:
					list_player_tmp[i] = ''
					list_wotd_tmp[i] = ''

			return_orange = utils.orange_letters(list_wotd_tmp,list_player_tmp)

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
			exit("Bravo")
	
	''' Fin de partie '''
	if attempt == 6:
		print("\nDommage, vous avez perdu. Le mot a trouver été :", word_of_the_day)

if __name__ == '__main__':
	main()