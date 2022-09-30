#! /usr/bin/env python3
import sys
import unittest
from unittest import mock
sys.path.insert(1, '/home/cedric/my_wordle')
import service_api
import utils
import gestion_exception


def get_mot_mock(*args, **kwargs):
	class MockResponse:
		def __init__(self, json_data, status):
			self.json_data = json_data
			self.status_code = status

		def json(self):
			return self.json_data

	list_wrong_word = ['bonjourr', 'vendreddi']

	if any(wrong_word in args[0] for wrong_word in list_wrong_word):
		return MockResponse({"error":"pas de résultats"}, 200)
	
	return MockResponse({"mot": 'VENDREDI'}, 200)


def get_mot_du_jour_mock_Basic_Cases(*args, **kwargs):
	class MockResponse:
		def __init__(self, json_data, status):
			self.json_data = json_data
			self.status_code = status

		def json(self):
			return self.json_data

	return MockResponse({'mot': 'FASTE'}, 200)


def get_mot_du_jour_mock_Error_Cases(*args, **kwargs):
	class MockResponse:
		def __init__(self, json_data, status):
			self.json_data = json_data
			self.status_code = status

		def json(self):
			return self.json_data

	raise gestion_exception.HTTPException('\nImpossible de selectionner le mot du jour. Erreur HTTP', 418)


class TestUtilsBasicCases(unittest.TestCase):

	# Constructor
	def __init__(self, *args, **kwargs):
		super(TestUtilsBasicCases, self).__init__(*args, **kwargs)
		self.service = service_api.ServiceAPI()
		self.wotd = 'VENDREDI'

		# self.mock_service = service_api.ServiceAPI()
		# self.mock_service.is_valid = mock.MagicMock(side_effect = self.is_valid_mock)
		
	# # Execute before each methods
	# def setUp(self):

	# # Execute after each methods
	# def tearDown(self):
	# 	self.wotd = "" 

	@mock.patch('requests.Session.get', side_effect=get_mot_mock)
	def test_given_an_existing_word_when_checking_word_validity_then_should_be_OK(self,mock_get):
		self.assertTrue(self.service.is_valid('bonjour', self.service.api_key))

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

	@mock.patch('requests.Session.get',side_effect=get_mot_du_jour_mock_Basic_Cases)
	def test_given_nothing_when_get_word_of_the_day_then_should_return_a_valid_word(self, mock_get):
		wotd = 'FASTE'
		self.assertEqual(wotd, self.service.get_word_of_the_day(self.service.api_key))


class TestUtilsErrorCases(unittest.TestCase):

	# Constructor
	def __init__(self, *args, **kwargs):
		super(TestUtilsErrorCases, self).__init__(*args, **kwargs)
		self.service = service_api.ServiceAPI()
		# self.wotd = self.service.get_word_of_the_day(self.service.api_key)
		self.wotd = 'VENDREDI'

	# # Execute before each methods
	# def setUp(self):

	# # Execute after each methods
	# def tearDown(self):
	# 	self.wotd = ""

	@mock.patch('requests.Session.get', side_effect=get_mot_mock)
	def test_given_a_wrong_word_when_checking_word_validity_then_should_be_KO(self, mock_get):
		self.assertFalse(self.service.is_valid('bonjourr', self.service.api_key))

	def test_given_a_wrong_word_of_the_day_when_checking_word_of_the_day_then_should_be_KO(self):

		self.assertFalse(utils.find_word_of_the_day('aaaa', self.wotd))
	
	def test_given_a_wrong_wotd_when_checking_if_the_letters_are_the_same_with_wotd_should_be_KO(self):
		
		l = [var for var in range(0, len(self.wotd))]
		self.assertNotEqual(l[::-1], utils.green_letters(self.wotd, self.wotd))

	def test_given_a_player_word_when_checking_if_the_letters_are_in_the_wotd_but_not_at_the_good_place_should_be_KO(self):
		player_word = 'VALSE'
		wotd = 'AIGLE'
		self.assertNotEqual([1,2,4], utils.orange_letters(wotd, player_word))

	def test_given_a_player_word_with_redundant_char_when_wotd_does_not_then_should_not_have_only_first_letter_in_orange(self):
		player_word = 'ELIME'
		wotd = 'AIGLE'
		self.assertNotEqual([0,1,2,4], utils.orange_letters(wotd, player_word))

	@mock.patch('requests.Session.get', side_effect = get_mot_du_jour_mock_Error_Cases)
	def test_given_nothing_when_getting_word_of_the_day_then_should_raise_an_exception(self, get_mock):
		with self.assertRaises(gestion_exception.HTTPException): 
			self.service.get_word_of_the_day(self.service.api_key + 'D')

if __name__ == '__main__':
	unittest.main()