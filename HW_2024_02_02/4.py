#Задание 4:
number = int (input ("Введите трехзначное число:"))  # СОВЕТ: после int и input пробелы не нужны, лучше сделать так: int(input("Введите трехзначное число:"))
first_number = int(number/ 100)  # СОВЕТ: не забывайте ставить пробелы вокруг математических операторов, лучше сделать так: int(number / 100)
second_number = int (number/10)%10 # СОВЕТ: не забывайте ставить пробелы вокруг математических операторов, после int пробелы не нужны, лучше сделать так: int(number / 10) % 10
last_number = int (number % 10)  # СОВЕТ: после int пробелы не нужны, лучше сделать так: int(number % 10)
print (
    f'Сумма цифр  = {first_number + second_number + last_number}',
    f'Произведение цифр  = {first_number * second_number * last_number}',
    sep = '\n'
) # СОВЕТ: после print пробелы не нужны

# Внимательно читайте задание целиком, нужно было так же скопировать пример ввода и пример вывода, тем не менее в первый раз засчитываю. =)

# Пример ввода:
#     333

# Пример вывода:
#     Сумма цифр = 9
#     Произведение цифр = 27
