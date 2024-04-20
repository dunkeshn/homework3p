# Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов

def sum_chetn1(n: int) -> int:
    sum = 0
    for i in range(2, n, 2):
        sum += i
    return sum

def sum_chetn2(n: int) -> int:
    sum = 0
    i = 2
    while i < n:
        sum += i
        i += 2
    return sum


if __name__ == '__main__':
    n = int(input('Введите число n: '))
    print(f'Подсчет суммы четных чисел первым способом: {sum_chetn1(n)}')
    print(f'Подсчет суммы четных чисел вторым способом: {sum_chetn2(n)}')
