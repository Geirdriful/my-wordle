#! /usr/bin/env python3
import unittest
import utils
import warnings

class TestUtils(unittest.TestCase):
	
	def test_search_player_word(self):

		self.assertTrue(utils.search_player_word('bonjour'))
		self.assertFalse(utils.search_player_word('bonjourr'))

	def test_find_word_of_the_day(self):

		warnings.simplefilter("ignore", ResourceWarning)
		wotd = utils.get_word_of_the_day()
		self.assertTrue(utils.find_word_of_the_day(wotd, wotd))
		self.assertFalse(utils.find_word_of_the_day('aaaa', wotd))

if __name__ == '__main__':
	unittest.main()