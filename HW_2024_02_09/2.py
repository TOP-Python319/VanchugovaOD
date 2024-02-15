# Написать программу, которая проверяет делится ли одно число на другое нацело. 
# Два целых числа программа должна по очереди получить из stdin (пользовательский ввод).
# Необходимо соблюсти формат вывода, показанный в примере ниже.

number1 = int(input('Enter number:'))
number2 = int(input('Enter number:'))

if number1 % number2 == 0:
    print (
        f"{number1} делится на {number2}",
        f"частное: {int(number1 / number2)}",
        sep = '\n'
        )
else:
    print (       
        f"{number1} не делится на {number2}",
        f"неполное частное: {int(number1 / number2)}",
        f"остаток: {int(number1 % number2)}",
        sep = '\n'
        )

# Пример ввода 1: 
    # Enter number:12
    # Enter number:5
# Пример вывода 1:    
    # 12 не делится на 5
    # неполное частное: 2
    # остаток: 2


# Пример ввода 2: 
    # Enter number:15
    # Enter number:3
# Пример вывода 2:
    # 15 делится на 3
    # частное: 5
 