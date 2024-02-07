#Задание 4:
number = int (input ("Введите трехзначное число:"))
first_number = int(number/ 100)
second_number = int (number/10)%10
last_number = int (number % 10)
print (
    f'Сумма цифр  = {first_number + second_number + last_number}',
    f'Произведение цифр  = {first_number * second_number * last_number}',
    sep = '\n'
)