print(type(('hello',)))  # Кортеж всего из одного значения нуждается в запятой внутри скобок. Ею указывается, что
# данные значение является кортежем. Для чего нужен? Если требуется упорядоченная последовательность значений,
# которые не будут изменяться. Благодаря неизменности содержимого Python сможет реализовать ускорение работы кода.

print(type(('hello')))  # В противном случае - без запятой внутри скобок, Python будет полагать, что введено обычное
# значение и просто заключили это значение в скобки.

print(str(42))  # Вызвать функцию str(42) для возврата значения '42', являющегося строковым представлением целого
# числа 42.

print(tuple(['cat', 'dog', 5]))  # Функция tuple() возвращает переданные ей значения в виде кортежа.
print(list(('cat', 'dog', 5)))  # Функция list() возвращает версию переданного ей значения в виде списка.
print(list('hello'))

spam = 42  # Переменной spam сначала присваивается значение 42
cheese = spam  # Значение переменной копируется и присваивается переменной cheese
spam = 100  # Переменной spam присваивается новое значение, но это не отражается на cheese
print(spam)  # Различные переменные хранят различные значения
print(cheese)
