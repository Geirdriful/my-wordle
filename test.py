#! /usr/bin/env python3
import utils

def main():

	wotd = ['R','O','S','E','S']
	word_player = ['R','E','P','O','S']

	ret = utils.green_letters(wotd, word_player)
	ret.reverse()

	list_wotd_tmp = wotd.copy()
	list_player_tmp = word_player.copy()

	if ret:
		for i in ret:
			list_player_tmp[i] = ''
			list_wotd_tmp[i] = ''
	
	retour = utils.orange_letters(list_wotd_tmp,list_player_tmp)

	for l in range(0, len(word_player)):
		if l in ret:
			print("\033[0;32;40m" + word_player[l] + "\033[0m", end ='')
		elif l in retour:
			print("\033[0;33;40m" + word_player[l] + "\033[0m", end ='')
		else:
			print("" + word_player[l], end = '')
	print()
		


if __name__ == '__main__':
	main()