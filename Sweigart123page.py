supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):  # Выражение в функции range() позволяет коду в цикле иметь доступ к индексу (в виде
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])  # переменной i) и к значению по этому индексу
    # (предоставляемому выражением supplies[i]). Интерирование обеспечивается по всем индексам списка supplies,
    # независимо от количества содержащихся в нем значений.
