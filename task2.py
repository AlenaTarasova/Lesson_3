"""Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно
быть дубликатов."""

lst = [6, 6, 6, 8, 9, 4, 4, 5, 3, 3, 7, 8]

lst_unc = []
for el in lst:
    if lst.count(el) > 1:
        lst_unc.append(el)
print(list(set(lst_unc)))