# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод
#
# 8-5+2-1
# Вывод
# 4

lst = list(input('Введите арифметическое выражение: '))
res = int(lst[0])
for i in range(len(lst)):
    if lst [i] == '-':
        res -= int(lst[i + 1])
    elif lst [i] == '+':
        res += int(lst[i + 1])
    else:
        continue
print(res)
