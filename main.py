# Перемістити 0 в кінець
# lst = [1, 0, 0, 8, 7, 0, 4]
# print(lst)
#
# for i in lst:
#     if i == 0:
#         lst.remove(0)
#         lst.append(0)
# print(lst)

# Сума елементів з парними індексами
# lst = [0, 3, 0, 5, 7, 6, 5, 0]
# print(lst)
# print(lst[::2])
# s = 0
#
# for index in range(len(lst)):
#     if index % 2 == 0:
#         s += lst[index]
# print(s)
# p = s*lst[-1]
# print(p)

# список випадкових чисел
import random

lst = []

for _ in range(random.randint(3,10)):
    lst.append(random.randint(3, 10))
print(len(lst))
print(lst)
new_lst = [lst[0], lst[2], lst[-2]]
print(new_lst)








# for i in lst:
#     if i % 2 == 0:
#         result = sum(i)
# print("Сума значень :", result)