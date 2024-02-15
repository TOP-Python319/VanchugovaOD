# Написать программу, которая определяет, является ли год високосным.
# Если год является високосным, то программа должна вывести в stdout слово “да”. В противном случае должно быть выведено слово “нет”.
# Примечание: год является високосным, если его номер кратен 4, но одновременно не кратен 100, или если он кратен 400.

year = int(input('Enter year:'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ('да')
else: 
    print ('нет')    

# Пример ввода:
    # Enter year:2020
# Пример вывода:
    # да

# Пример ввода:
    # Enter year:1999
# Пример вывода:
    # неьт
