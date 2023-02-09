from players import Player
from funcs import load_random_word


def main():

    """ Основной код программы"""

# Заправшиваем данные пользователя и создаем объект класса
    user_name = input('Введите имя игрока\n')
    player = Player(user_name)
# Загружаем список слов и выбираем случайное слово помещая его в объект класса BasicWord
    word = load_random_word()
# Приветсвуем пользователя и даем задание
    print(f'Привет, {player.player_name}!\nСоставьте {word.len_subwords()} слов из слова {word.basic_word.upper()}\n'
          f'Слова должны быть не короче 3 букв\n'
          f'Чтобы закончить игру, угадайте все слова или напишите "stop"\nПоехали, ваше первое слово?')
# Запускаем цикл по которому пользователя запрашиют слова и выдают ответ.
# Цикл работает пока пользователь не угадает все слова
    while player.used_words_number() < word.len_subwords():
        user_word = input().lower()
        if user_word not in ["stop", "стоп"]:

            if word.check_word(user_word):
                if player.find_in_used(user_word):
                    print('Слово уже использовано')
                else:
                    player.used_word_append(user_word)
                    print(f'Верно {player.used_words} {player.used_words_number()}')

            else:
                print('Неверно')

        else:
            break

    print(f'\nИгра завершена, вы угадали {player.used_words_number()} слов!')


if __name__ == "__main__":
    main()
