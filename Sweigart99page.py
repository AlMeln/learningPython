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


print(getAnswer(random.randint(1, 9)))  # Поскольку возвращаемые значения могут передаваться
# в качестве аргументов другим вызываемым функциям три строки из Sweigart98page.py можно
# представить эквивалентом в одну строку. Вызов функции можно использовать в выражениях,
# поскольку это эквивалентно использованию возвращаемого значения функции.
