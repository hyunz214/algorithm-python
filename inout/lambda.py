# -*- coding: utf-8 -*-

list1 = {1, 2, 3, 4, 5, 6}
list2 = {6, 7, 8, 9, 10}

result = (lambda a, b: a + b)(list1, list2)

print(list(result))