#! /usr/bin/env python3
import requests
import gestion_exception
from datetime import date


class ServiceAPI(object):

    def __init__(self):
        ''' Initialisation'''
        self.session = requests.Session()

        with open('/home/cedric/my_wordle/api_key.txt', 'r') as f:
            self.api_key = f.read()

    ''' Recupere le mot du jour en utilisant sur l'api de dicolink (En se basant sur la date du jour)'''
    def get_word_of_the_day(self, api_key):

        today = date.today()
        header = {
            'Content-Type': 'application/json'
        }
        url = f'https://api.dicolink.com/v1/mots/motdujour?date={str(today)}&api_key={api_key}'

        with requests.Session() as session:
            response = session.get(url, headers=header)
            status_code = response.status_code

            if status_code == 200:
                return response.json()['mot'].upper()
            else:
                raise gestion_exception.HTTPException('\nImpossible de selectionner le mot du jour. Erreur HTML', status_code)

    ''' Trouve si le mot du joueur existe dans le dictionnaire francais. Si oui, le mot est valide, si non il est invalide> Utilise l'api de dicolink '''
    def is_valid(self, word, api_key):

        header = {
            'Content-Type': 'application/json'
        }
        url = f'https://api.dicolink.com/v1/mot/{str(word)}/definitions?limite=200&api_key={api_key}'

        with requests.Session() as session:
            response = session.get(url, headers=header)
            status_code = response.status_code

            if status_code == 200:
                if isinstance(response.json(), dict) and response.json().get('error'):
                    return False
                return True
            else:
                raise gestion_exception.HTTPException('\nLe mot propose n\'existe pas, erreur HTML', status_code)
