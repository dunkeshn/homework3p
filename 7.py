# Проверить, является ли строка палиндромом (зеркальная)

def palindrom(s: str) -> None:
    s = s.replace(' ', '')
    s = s.lower()
    if s == s[::-1]:
        print('Строка является палиндромом!')
    else:
        print('Строка НЕ является палиндромом!(')



if __name__ == '__main__':
    s = input('Введите строку: ')
    palindrom(s)
