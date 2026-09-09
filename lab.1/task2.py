#Средний №9
number = int(input("Введите трехзначное число: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

sum_digits = hundreds + tens + ones
product_digits = hundreds * tens * ones

print("Сумма цифр:", sum_digits)
print("Произведение цифр:", product_digits)
