#! /usr/bin/env python3
import unittest
import utils
import warnings

class TestUtils(unittest.TestCase):
	global wotd
	wotd = utils.get_word_of_the_day()

	''' Test si un mot existe dans le dictionnaire '''
	def test_search_player_word(self):

		self.assertTrue(utils.search_player_word('bonjour'))
		self.assertFalse(utils.search_player_word('bonjourr'))

	''' Test si le mot du joueur est le mot du jour '''
	def test_find_word_of_the_day(self):

		warnings.simplefilter("ignore", ResourceWarning)
		self.assertTrue(utils.find_word_of_the_day(wotd, wotd))
		self.assertFalse(utils.find_word_of_the_day('aaaa', wotd))
	
	''' Test le retour de green_letters (liste contenant les index des lettres a la bonne place)'''
	def test_green_letter(self):
		
		l = [var for var in range(0, len(wotd))]
		self.assertEqual(l, utils.green_letters(wotd, wotd))

	''' Test le retour de orange_letters (liste contenant les index des lettres mal placees)'''
	def test_orange_letter(self):

		l = [var for var in range(0, len(wotd))]
		self.assertEqual(l, utils.green_letters(wotd, wotd))

if __name__ == '__main__':
	unittest.main()