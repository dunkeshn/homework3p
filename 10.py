# Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]

def rev(s: str) -> None:
    for i in range(len(s) - 1, -1, -1):
        print(s[i])


if __name__ == '__main__':
    s = input('Введите строку: ')
    rev(s)