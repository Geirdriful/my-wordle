#! /usr/bin/env python3
import utils
import requests
import json
from datetime import date

def main():

	wotd = "TAROUPE"
	mot = "EPUORAT"
	print(utils.orange_letters(wotd,mot))


if __name__ == '__main__':
	main()
