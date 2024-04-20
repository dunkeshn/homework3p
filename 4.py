# Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()

def each_third_element(l: list) -> None:
    for i in list(enumerate(l, 1)):
        if i[0] % 3 == 0:
            print(f'{i[1]}, индекс: {i[0]}')


if __name__ == '__main__':
    l = [i for i in range(1, 100)]
    each_third_element(l)
