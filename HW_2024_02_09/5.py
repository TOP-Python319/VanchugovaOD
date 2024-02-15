# Написать программу, которая проверяет корректность хода шахматной ладьи.
# Примечание: шахматная ладья ходит по горизонтали или вертикали.

square1 = input('Введите номер клетки шахматной доски:')
square2 = input('Введите номер клетки шахматной доски:')
num1 = int(square1[1])
num2 = int(square2[1])
letter1 = ord(square1[0])-ord("a")
letter2 = ord(square2[0])-ord("a")

if letter1 == letter2 or num2 == num1:
    print ('yes')
else:
    print ('no')    


# Пример ввода:
#     a3
#     e5

# Пример вывода:
#     no    
