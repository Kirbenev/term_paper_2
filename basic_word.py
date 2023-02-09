class BasicWord():
    """
    Класс "Исходное слово"
    **Поля:**
      -исходное слово
      -набор допустимых подслов

    **Методы:**
      -проверка введенного слова в списке допустимых подслов (вернет bool)
      -подсчет количества подслов (вернет int)

    При инициализации задается исходное слово и набор допустимых слов
    """

    def __init__(self, basic_word, subwords):
        self.basic_word = basic_word
        self.subwords = subwords

    def __repr__(self):
        return f"BasicWord('{self.basic_word}', {self.subwords})"

    def check_word(self, word):
        """ проверка введенного слова в списке допустимых подслов (вернет bool)"""
        if word in self.subwords:
            return True
        else:
            return False

    def len_subwords(self):
        """подсчет количества подслов (вернет int)"""
        return len(self.subwords)