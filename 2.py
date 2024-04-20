# Найти самое длинное слово из массива. Реализовать двумя видами циклов

def longest_word1(l: list) -> str:
    max_length = 0
    longest_word = ''
    for word in l:
        if max_length < len(word):
            max_length = len(word)
            longest_word = word
    return longest_word

def longest_word2(l: list) -> str:
    max_length = 0
    longest_word = ''
    i = 0
    while i < len(l):
        if max_length < len(l[i]):
            max_length = len(l[i])
            longest_word = l[i]
        i += 1
    return longest_word


if __name__ == '__main__':
    l = ['python', 'pep8', 'monty', 'netherlands']
    print(f'Поиск самого первого слова первым способом: {longest_word1(l)}')
    print(f'Поиск самого первого слова вторым способом: {longest_word2(l)}')
