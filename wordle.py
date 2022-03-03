#! /usr/bin/env python3
import utils
import random

def main():

	''' Déclaration variables '''
	list_lettres_unique = list()
	list_letter_of_the_day = list()
	
	word_player = ""
	attempt = 1 

	''' Selection d'un mot parmi la liste '''
	word_list = utils.open_file_and_read('mots.txt')

	number = random.randint(0, len(word_list))
	# word_of_the_day = word_list[number]
	word_of_the_day = 'FRENE'
	print("Selection d'un mot de 5 lettres ...")
	for index in range(0, len(word_of_the_day)):
		list_letter_of_the_day.append(word_of_the_day[index])
	
	''' tant que le joueur n'a pas trouvé et qu'il n'a pas fait 6 tentatives '''
	while word_player.upper() != word_of_the_day and attempt < 7:
		''' Entrée clavier par le joueur '''
		word_player = input("\nProposition ? ")
		
		''' Bingo, c'est le mot du jour'''
		if word_player == word_of_the_day:
			print("\033[0;32;40m" + word_of_the_day + "\033[0m")
			print("Bravo")
		else:
			''' Découpage du mot du joueur et ajout dans une liste '''
			list_letter_of_the_player = list()
			for index in range(0, len(word_of_the_day)):
				list_letter_of_the_player.append(word_player[index])

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
					print("\033[0;32;40m" + word_player[l] + "\033[0m", end ='')
				elif l in return_orange:
					print("\033[0;33;40m" + word_player[l] + "\033[0m", end ='')
				else:
					print("" + word_player[l], end = '')
		attempt = attempt + 1
	
	''' Fin de partie '''
	if attempt == 7:
		print("\nDommage, vous avez perdu. Le mot a trouver été :", word_of_the_day)

if __name__ == '__main__':
	main()