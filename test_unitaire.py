#! /usr/bin/env python3
import unittest
import utils
import warnings

# warnings.simplefilter("ignore", ResourceWarning)
# class TestUtils(unittest.TestCase):

class ChaineDeCaractereTest(unittest.TestCase):

	def test_search_player_word(self):
		warnings.simplefilter("ignore", ResourceWarning)
		self.assertTrue(utils.search_player_word('bonjour'))
		self.assertFalse(utils.search_player_word('bonjourr'))

if __name__ == '__main__':
	unittest.main()