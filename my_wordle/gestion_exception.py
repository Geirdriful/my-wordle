#! /usr/bin/env python3
import utils
import requests
from datetime import date

class HTMLException(Exception):

	def __init__(self, message, value):
		super().__init__(message, value)
		print(message, value)