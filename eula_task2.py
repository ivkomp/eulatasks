"""Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона."""

#случае с рекурсией получим ошибку превышения максимального количества рекурсий

"""def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

print(fibonacci(999))"""


fib1 = fib2 = 1
element = int(input())

for n in range(int(element-2)):
    cur = fib1 + fib2
    fib1 = fib2
    fib2 = cur
print(fib2)