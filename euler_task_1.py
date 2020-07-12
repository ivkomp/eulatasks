"""Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""

#create list
numb_list = []
count_input = int(input())
count = 0

#append list
for i in range(count_input):
    numb_list.append(i)

#proces
for x in numb_list:
    if numb_list[x] % 3 == 0 or numb_list[x] % 5 == 0:
        count += numb_list[x]

#resalt
print(count)