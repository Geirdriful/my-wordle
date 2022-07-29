#! /usr/bin/env python3
import unittest
import sys
sys.path.insert(1, '/home/Cédric/Projet_Wordle/my_wordle')
import service_api
import utils
# import my_wordle.utils

import warnings

class TestUtilsBasicCases(unittest.TestCase):

	# Constructor
	def __init__(self, *args, **kwargs):
		super(TestUtilsBasicCases, self).__init__(*args, **kwargs)
		self.service = service_api.ServiceAPI()
		self.wotd = self.service.get_word_of_the_day()

	# # Execute before each methods
	# def setUp(self):
		
	
	# # Execute after each methods
	# def tearDown(self):
	# 	self.wotd = ""

	def test_given_an_existing_word_when_checking_word_validity_then_should_be_OK(self):
		self.assertTrue(self.service.is_valid('bonjour'))

	''' Test si le mot du joueur est le mot du jour '''
	def test_find_word_of_the_day(self):

		# warnings.simplefilter("ignore", ResourceWarning)
		self.assertTrue(utils.find_word_of_the_day(self.wotd, self.wotd))
		self.assertFalse(utils.find_word_of_the_day('aaaa', self.wotd))
	
	''' Test le retour de green_letters (liste contenant les index des lettres a la bonne place)'''
	def test_green_letter(self):
		
		l = [var for var in range(0, len(self.wotd))]
		self.assertEqual(l, utils.green_letters(self.wotd, self.wotd))

	''' Test le retour de orange_letters (liste contenant les index des lettres mal placees)'''
	def test_orange_letter(self):

		l = [var for var in range(0, len(self.wotd))]
		self.assertEqual(l, utils.green_letters(self.wotd, self.wotd))


class TestUtilsErrorCases(unittest.TestCase):

	# Constructor
	def __init__(self, *args, **kwargs):	
		super(TestUtilsErrorCases, self).__init__(*args, **kwargs)
		self.service = service_api.ServiceAPI()
		self.wotd = self.service.get_word_of_the_day()

	# # Execute before each methods
	# def setUp(self):

	# # Execute after each methods
	# def tearDown(self):
	# 	self.wotd = ""

	def test_given_a_wrong_word_when_checking_word_validity_then_should_be_KO(self):
		self.assertFalse(self.service.is_valid('bonjourr'))




if __name__ == '__main__':
	unittest.main()