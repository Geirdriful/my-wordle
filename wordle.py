#! /usr/bin/env python3
import utils
import random

def main():

	word_list = utils.open_file_and_read('mots.txt')

	number = random.randint(0, len(word_list))
	word_of_the_day = word_list[number]
	print("Selection d'un mot de 5 lettres ...")
	# print("\033[0;33;40m " + word_of_the_day, "\033[0m")
	print(word_of_the_day)

	letter_of_the_day_list = list()
	for index in range(0, len(word_of_the_day)):
		letter_of_the_day_list.append(word_of_the_day[index])
	
	word_player = ""
	attempt = 1

	while word_player.upper() != word_of_the_day and attempt < 7:
		word_player = input("\nProposition ? ")
		if word_player == word_of_the_day:
			print("\033[0;32;40m" + word_of_the_day + "\033[0m")
			print("Bravo")
		else:
			for index in range(0, len(word_player)):
				letter = word_player[index]
				if letter in letter_of_the_day_list:
					if index == letter_of_the_day_list.index(letter):
						print("\033[0;32;40m" + letter.upper() + "\033[0m", end = '')
					else:
						print("\033[0;33;40m" + letter.upper() + "\033[0m" , end = '')
				else:
					print("" + letter.upper(), end = '')
			attempt = attempt + 1

	

if __name__ == '__main__':
	main()