# Инструкция continue используется в циклах для передачи управления в начало цикла,
# где условие вычисляется заново.

while True:  # Цикл while продолжает выполняться до тех пор, пока условие остается истинным.
    print('Как тебя зовут?')
    name = input()
    if name != 'Джо':  # Если пользователь вводит любое другое имя, кроме "Джо",
        continue  # то инструкция заставляет программу перейти в начало цикла. В случае прохождения инструкции if
    print('Привет, Джо. Введешь пароль? (Это связано с рыбой.)')  # запрашивает ввод пароля.
    password = input()
    if password == 'swordfish':  # Если пользователь вводит пароль swordfish,
        break  # то выполняется инструкция break. Программа покидает цикл while и
print('Доступ предоставлен.')  # выводит на экран сообщение о доступе. В противном случае управление выполнением
# программы передается циклу while, возвращаясь в его начало.
