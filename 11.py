# Напечатать календарь месяца, предполагая, что месяц начинается в понедельник и имеет 31 день

def print_calendar(l: list) -> None:
    j = 0
    for i in range(len(l)):
        if j == 7:
            print('')
            j = 0
        if l[i] < 10:
            print(f' {l[i]} ', end='')
        else:
            print(f'{l[i]} ', end='')
        j += 1



if __name__ == '__main__':
    print('Пн Вт Ср Чт Пт Сб Вс')
    calendar = [i for i in range(1, 32)]
    print_calendar(calendar)