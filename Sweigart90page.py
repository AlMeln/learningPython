import random  # Импортировать при помощи инструкции import модуль random
for i in range(5):
    print(random.randint(1, 10))  # Функцией random.randint() возвратить случайное число, лежащее в диапазоне между
    # двумя целочисленными значениями, которые переданы функции в качестве аргументов. Функция randint() находится в
    # модуле random, поэтому его имя должно указываться в виде префикса (через точку) перед именем функции, чтобы Python
    # мог определить, что данную функцию следует искать в модуле random.
