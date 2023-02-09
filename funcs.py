import random, json, requests
from basic_word import BasicWord


def load_random_word():

    """ Функция загружает список полей для Класса вопросы с внешеннего сервера и возвращает список объктов класа Basicword"""

    response = requests.get('https://www.jsonkeeper.com/b/MA7X')
    word = random.choice(response.json())
    return BasicWord(word['word'], word['subwords'])

# def load_random_word():
#
#     """ (на случай если jsonkeeper не работает) Функция загружает список полей для Класса вопросы из JSON Файла  и возвращает список объктов класа Basicword"""
#
#     with open('data.json') as f:
#         raw_json = f.read()
#     word = random.choice(json.loads(raw_json))
#     return BasicWord(word['word'], word['subwords'])
