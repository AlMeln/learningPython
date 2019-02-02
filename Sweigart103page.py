# Локальные переменные одной функции полностью отделены от локальных переменных другой функции.


def spam():  # Из последней строки кода вызвать функцию spam() и содается локальная область
    # видимости. Новая локальная область видимости создается всякий раз, когда вызывается функция,
    # включая случаи, когда функция вызывается из другой функции.
    eggs = 99  # Локальной переменной eggs присвоить значение 99.
    bacon()  # Затем вызвать функцию bacon() и создать вторую локальную область видимости. В одно и то же время могут
    # существовать несколько локальных областей видимости. После возврата из функции bacon() ее локальная область
    # видимости уничтожается.
    print(eggs)


def bacon():
    ham = 101  # Создать новую локальную область видимости и установить значение локальной
    # переменной ham равным 101.
    eggs = 0  # Создать локальную переменную eggs равную 0, которая отличается от eggs в
    # локальной видимости функции spam().


spam()