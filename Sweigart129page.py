spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')  # При наличии в списке нескольких одинаковых значений, будет удалено лишь то из них, которое
# встречается первым.
print(spam)

spam = [2, 5, 3.14, 1, -7]
spam.sort()  # Сортировка списков, содержащих числа или строки.
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)  # Задать сортировку в обратном порядке, указав именованный аргумент reverse со значением
# True при вызове метода sort().
print(spam)
