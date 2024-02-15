# Написать программу, которая подсчитывает сумму только положительных чисел.
# Три числа программа должна по очереди получить из пользовательского ввода (stdin — стандартный поток ввода).

number1 = float(input('Enter number:'))
number2 = float(input('Enter number:'))
number3 = float(input('Enter number:'))
sum = 0

if number1 > 0:
    sum += number1
if number2 > 0:
    sum += number2
if number3 > 0:
    sum += number3
print(sum)

# Пример ввода:
# Enter number:4
# Enter number:-7
# Enter number:8


# Пример вывода:
#     12.0



