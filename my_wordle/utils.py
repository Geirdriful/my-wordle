#! /usr/bin/env python3


def green_letters(wotd, player_word):
    ''' Detection des lettres vertes. Ces lettres sont presentes dans le WOTD et sont a la bonne place'''
    list_indexes = list()
    for index_player_word, char_player_wotd in enumerate(player_word):
        if char_player_wotd in wotd and char_player_wotd == wotd[index_player_word]:
            list_indexes.append(index_player_word)
    return list_indexes


def orange_letters(wotd, player_word):
    ''' Detection des lettres oranges. Ces lettres sont presente dans le WOTD mais ne sont pas a la bonne place'''
    list_indexes = list()

    for index_player_word, char_player_word in enumerate(player_word.upper()):
        if char_player_word in wotd and char_player_word != wotd[index_player_word]:
            count_wotd = wotd.count(char_player_word)
            count_player_word = player_word.count(char_player_word)

            if (count_player_word >= count_wotd) and index_player_word == player_word.find(char_player_word):
                list_indexes.append(index_player_word)
            elif (count_player_word <= count_wotd) and index_player_word == player_word.find(char_player_word):
                list_indexes.append(index_player_word)

    return list_indexes


def find_word_of_the_day(word_player, word_of_the_day):
    if word_player.upper() == word_of_the_day:
        return True
    else:
        return False
