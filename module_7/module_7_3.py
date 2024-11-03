from pprint import pprint


class WordsFinder:

    def __init__(self, *file_names):
        self.all_words = {}
        self.file_names = file_names

    def get_all_words(self):
        for name in self.file_names:
            with open(name) as file:
                lst_word = []
                for line in file:
                    slug = ''
                    for s in line.lower():
                        if s in '!?:;.,=-':
                            slug += ''
                        elif s in '\n':
                            slug += ''
                        else:
                            slug += s
                    lst_word += slug.split(' ')
            self.all_words[name] = lst_word
        return self.all_words

    def find(self, word):
        dict1 = {}
        for key, value in self.all_words.items():
            i = 0
            for s in value:
                i += 1
                if s == word.lower():
                    break
            dict1[key] = i
        return dict1

    def count(self,word):
        dict2 = {}
        for key, value in self.all_words.items():
            i = 0
            for s in value:
                if s == word.lower():
                    i += 1
            dict2[key] = i
        return dict2


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))