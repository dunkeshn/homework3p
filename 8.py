# Определить, содержит ли список дубликаты

def duplicates(l: list) -> None:
    if len(l) == len(set(l)):
        print('Список не имеет дубликатов!')
    else:
        print('В списке присутствуют дубликаты!(')


if __name__ == '__main__':
    l = ["1", "2", "3", "4", "5", "4"]
    duplicates(l)