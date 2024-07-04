import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self.all_words = {}

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r') as file:
                words = file.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
                self.all_words[file_name] = words
        return self.all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word)
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word)
            result[name] = count
        return result


# Пример использования
finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(finder.get_all_words())
print(finder.find('word1'))
print(finder.count('word2'))
