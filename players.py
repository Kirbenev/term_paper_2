class Player():
    """
        Класс "Игрок"

        **Поля:**
          -имя пользователя
          -использованные слова пользователя

        **Методы:**
          -получение количества использованных слов (возвращает int)
          -добавление слова в использованные слова (ничего не возвращает)
          -проверка использования данного слова до этого (возвращает bool)

        При инициализации задается только имя игрока
    """

    def __init__(self, player_name, used_words=[]):
        self.player_name = player_name
        self.used_words = used_words

    def __repr__(self):
        return f"Player('{self.player_name}', {self.used_words})"

    def used_words_number(self):
        """получение количества использованных слов (возвращает int)"""
        return len(self.used_words)

    def used_word_append(self, word):
        """добавление слова в использованные слова (ничего не возвращает)"""
        self.used_words.append(word)

    def find_in_used(self, word):
        """проверка использования данного слова до этого (возвращает bool)"""
        if word in self.used_words:
            return True
        else:
            return False