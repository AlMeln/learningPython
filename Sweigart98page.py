import random  # Python в первую очередь импортирует модуль random.


def getAnswer(answerNumber):  # Определить функцию getAnswer(). Функция лишь определяется.
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again leter'
    elif answerNumber == 6:
        return 'Concentrate and ask againg'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)  # Вызвать функцию random.randint() с двумя аргументами - 1 и 9.
# Функцией возвратить случайное целое число, принадлежащее диапазону чисел от 1 до 9
# (включая сами эти значения), и это число сохранить в переменной r.
fortune = getAnswer(r)  # Вызвать функцию getAnswer() и передать ей переменную r в качестве
# аргумента. Выполнение программы переходит в начало, когда дается команда вызвать функцию
# getAnswer() передав ей в качестве аргумента одно из множества возможных строковых занчений,
# зависящих от значения answerNumber. Далее возвращенную строку присвоить переменной fortune,
print(fortune)  # которая затем передается функции print() и выводится на экран.
