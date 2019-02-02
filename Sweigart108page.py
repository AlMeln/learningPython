def spam(divideBy):
    return 42 / divideBy


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Сообщение об ошибке "ZeroDivisionError: division by zero" выводится всякий раз при попытке разделить число на 0.
# По указанному в ообщении об ошибке номеру строки
# ("File "/.../Sweigart108page.py", line 7, in <module>print(spam(0))")
# можно легко определить, что виновницей является инструкция return функции spam() - "line 2, in spam return 42 /
# divideBy".