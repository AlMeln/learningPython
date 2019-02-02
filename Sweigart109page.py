# Ошибки можно обрабатывать с помощью инструкций try и except [ɪkˈsept]. Код, относительно которого есть
# подозрения, что он приведет к ошибке, помещается в блок try. В случае возникновения ошибки,
# выполнение программы передается в начало блока except.

def spam(divideBy):
    try:  # Поместить код с 108 страницы в блок инструкции try.
        return 42 / divideBy
    except ZeroDivisionError:  # Обработать соответствующую ошибку в блоке инструкции except.
        print('Error: Invalid argument.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
