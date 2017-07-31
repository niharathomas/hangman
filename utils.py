import settings
import requests


def get_random_word(length=settings.DEFAULT_WORD_LENGTH):
    '''
    Returns a word of the desired length obtained from an external API call
    :param length: Length of word to be guessed
    :return: Word of desired length
    '''
    url = settings.RANDOM_WORD_API + str(length)
    return requests.get(url).text


def get_word_meaning(word):
    '''
    Returns the meaning of the word
    :param word: Current game word
    :return: String containing the meaning of the current game word
    '''
    response = requests.get(settings.WORDS_API + word).json
    return response


def get_displayed_word(word, boolean_list):
    '''
    Returns a boolean list with True corresponding to all the correctly guessed characters and 
    False for the hidden characters to be displayed with un-guessed characters hidden
    :param word: Current game word
    :param boolean_list: Cencored list of characters in the list
    :return: 
    '''
    return [letter if boolean_list[i] else '_' for i, letter in enumerate(word)]
