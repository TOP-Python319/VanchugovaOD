# Написать программу, которая проверяет корректность хода шахматного короля.
# Примечание: шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.

square1 = input('Введите номер клетки шахматной доски:')
square2 = input('Введите номер клетки шахматной доски:')
num1 = int(square1[1])
num2 = int(square2[1])
letter1 = ord(square1[0])-ord("a")
letter2 = ord(square2[0])-ord("a")

if (-1 <= num2 - num1 <= 1 or num2 == num1) and (letter1 == letter2 or -1 <= letter2 - letter1 <= 1):
    print ('yes')
else:
    print ('no')    

# Пример ввода:
#     b3
#     e6

# Пример вывода:
#     no        