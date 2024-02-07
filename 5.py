#Задание 5:
# 1 миля = 1.61 км
# f'{12.358:.2f}' >>>  '12.36'  - не понимаю как он работает 

first_number = int (input ("Введите цифру:"))
second_number = int (input ("Введите число после запятой:"))

mile = float(f"{first_number}.{second_number}")
km = mile * 1.61
print(f"{mile} миль = {km:.1f} км")

#mile2 = first_number + second_number/10**len(str(second_number))
