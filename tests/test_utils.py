#! /usr/bin/env python3
import unittest
import sys
sys.path.insert(1, '/home/cedric/my_wordle')
import service_api
import utils
from unittest.mock import MagicMock

class TestUtilsBasicCases(unittest.TestCase):

	def is_valid_mock(self, value):
		if value == 'bonjour':
			return True
		return False

	# Constructor
	def __init__(self, *args, **kwargs):
		super(TestUtilsBasicCases, self).__init__(*args, **kwargs)
		self.service = service_api.ServiceAPI()
		self.wotd = 'VENDREDI'

		self.mock_service = service_api.ServiceAPI()
		self.mock_service.is_valid = MagicMock(side_effect = self.is_valid_mock)
		
	# # Execute before each methods
	# def setUp(self):

	# # Execute after each methods
	# def tearDown(self):
	# 	self.wotd = ""

	def test_given_an_existing_word_when_checking_word_validity_then_should_be_OK(self):
		self.assertTrue(self.mock_service.is_valid('bonjour'))

	def test_given_the_real_word_of_the_day_when_checking_word_of_the_day_then_should_be_OK(self):
		
		self.assertTrue(utils.find_word_of_the_day(self.wotd, self.wotd))
	
	def test_given_the_real_wotd_when_checking_if_the_letters_are_at_the_good_place_compare_to_wotd_then_should_be_ok(self):
		
		l = list(range(len(self.wotd)))
		self.assertEqual(l, utils.green_letters(self.wotd, self.wotd))

	def test_given_the_wotd_when_checking_if_the_letters_are_in_the_wotd_but_not_at_the_good_place_should_be_ok(self):
		player_word = 'VALSE'
		wotd = 'AIGLE'
		self.assertEqual([1,2], utils.orange_letters(wotd, player_word))

	def test_given_a_player_word_with_redundant_char_when_wotd_does_not_then_should_have_only_first_letter_in_orange(self):
		player_word = 'ELIME'
		wotd = 'AIGLE'
		self.assertEqual([0, 1, 2], utils.orange_letters(wotd, player_word))

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

	def test_given_a_wrong_word_of_the_day_when_checking_word_of_the_day_then_should_be_KO(self):

		self.assertFalse(utils.find_word_of_the_day('aaaa', self.wotd))
	
	def test_given_a_wrong_wotd_when_checking_if_the_letters_are_the_same_with_wotd_should_be_KO(self):
		
		l = [var for var in range(0, len(self.wotd))]
		self.assertNotEqual(l[::-1], utils.green_letters(self.wotd, self.wotd))

	def test_given_a_player_word_when_checking_if_the_letters_are_in_the_wotd_but_not_at_the_good_place_should_be_KO(self):
		player_word = 'VALSE'
		wotd = 'AIGLE'
		print(utils.orange_letters(wotd, player_word))
		self.assertNotEqual([0,3,4], utils.orange_letters(wotd, player_word))

	def test_given_a_player_word_with_redundant_char_when_wotd_does_not_then_should_have_only_first_letter_in_orange(self):
		player_word = 'ELIME'
		wotd = 'AIGLE'
		print(utils.orange_letters(wotd, player_word))
		self.assertNotEqual([3,4], utils.orange_letters(wotd, player_word))

if __name__ == '__main__':
	unittest.main()