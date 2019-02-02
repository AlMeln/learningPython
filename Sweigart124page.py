print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])  # Оператор in позволяет определить, находится ли какое-либо
# значение в списке. Оператор in используется в выражениях, соединения два значения: то, поиск которого выполняется
# в списке, и список, в котором это значение может находиться.

spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)  # Результатов вычисления выражений является булевое значение.
print('howdy' not in spam)
print('cat' not in spam)

myPets = ['Zophie', 'Pooka', 'Fat-tail', 'Chara']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do no have a pet named ' + name)
else:
    print(name + ' is my pet.')
