int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

# print ("int_a ", id (int_a))
#
# print ("str_b", id (str_b))
# print ("set_c", id (set_c))
#
# print ("lst_d", id (lst_d))
#
# print ("dict_e", id (dict_e))


# lst_d = [1, 2, 3, 4, 5]
# print ("lst_d", id(lst_d))

# print("int_a", type(int_a))
#
# print("str_b", type(str_b))
#
# print("set_c", type(set_c))
#
# print("lst_d", type(lst_d))
#
# print("dict_e", type(dict_e))


#
# print("int_a", isinstance(int_a, int))
#
#
# print("str_b", isinstance(str_b, (int, float)))
#
# print("set_c", isinstance(set_c, set))
#
# print("lst_d", isinstance(lst_d, set))
#
# print("dict_e", isinstance(dict_e, set))
#
#
# print("Anna has {1} apples and {0} peaches." .format(5, 6))
#
#
# apples = 10
#
# peaches = 7



# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# list_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
#
#
# print(list_comp)












# print("Anna has {apples} apples and {peaches} peaches." .format(apples=10, peaches=7))

# number = "7"
#
# second_number = "6"
#
# print("Anna has %s, apples and %s peaches." % (number, second_number))
#
#
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#         print(lst)
#
#
# print("Anna has {0:5} apples and {1:3} peaches." .format(17, 15))

# four = 4
# five = 5
#
#  print(f"Anna has {four} apples and {five} peaches.")
#
#
# lst = []
#
# for number in range(25):
#
#     lst.append(number)
#
# print(lst)
#
# lst_comp = []

# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#
# print(list_comprehension)


# lst = []
#
# for num in range(10):
#
#     if num % 2 == 0:
#         lst.append(num // 2)
#
#     else:
#
#         lst.append(num * 10)
#         print(lst)



# dct = {}
#
# for x in range(10):
#
#    if x**3 % 4 == 0:
#
#     dct[x] = x**3
# print(dct)


# dct = {}
#
# for x in range(10):
#
#    if x**3 % 4 == 0:
#
#      dct[x] = x**3
#
#    else:
#
#      dct[x] = x
#
# print(dct)


# foo = lambda x, y: x if x < y else y
#
# print(foo)



# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# print(foo)


#
# def foo(x, y, z):
#     if y < x and x > z:
#      return z
#     else:
#      return y
#
#     print(foo)


# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# print(sorted(lst_to_sort, reverse=True))


# def foo(x):
#     return x*2
#
# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# new_list = list(map(foo, lst_to_sort))
# print(new_list)


# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
#
# list_A = (list(map(lambda x, y: x**y, list_A, list_B)))
#
# print(list_A, '=', list_B)

# from functools import reduce
#
# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# sum_lst_to_sort = reduce(lambda x, y: x + y, lst_to_sort)
#
# print(sum_lst_to_sort)


# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# new_lst_to_sort = list(filter(lambda x: x % 2 ==0, lst_to_sort))
#
# print(new_lst_to_sort)

#



list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

print(list(filter(lambda x: x in list_1, list_2)))
