# Удалить все дубликаты из списка без использования дополнительных структур.
# Реализовать двумя видами циклов, для удаления можно использовать pop() либо del

def del_duplicates1(l: list) -> list:
    for i in range(len(l)):
        if i >= len(l):
            break
        if l.count(l[i]) > 1:
            del l[i]
            i -= 1
    return l

def del_duplicates2(l: list) -> list:
    i = 0
    while i < len(l):
        if l.count(l[i]) > 1:
            del l[i]
            continue
        i += 1
    return l

if __name__ == '__main__':
    l = [1, 2, 3, 1, 2, 3, 4, 5, 6, 6]
    print(l)
    res1 = del_duplicates1(l)
    print(res1)
    res2 = del_duplicates2(l)
    print(res2)
