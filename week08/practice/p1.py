# Are a, b, c all the same?
# a = 9453252335432530000000000000000000000000
# b = 9453252335432530000000000000000000000000
a = 954
b = 954
print(type(a))
print(type(b))
print(id(a))
print(id(b))
# c = a
# print(id(c))
#
# # What's the value of a, b, c?
# a = 456
# print(id(a))
# c = 789
# c = b = a
# print(a, b, c)
#
# # What's the value of x, y
# x = [1, 2, 3]
# y = x
# x.append(4)
# print(x) # [1, 2, 3, 4]
# print(y) # [1, 2, 3, 4]
#
# # What's the value of a, b
# a = [1, 2, 3]
# b = a
# a = [4, 5, 6]
# print(a)  # [4, 5, 6]
# print(b)  # [1, 2, 3]
#
# # What's the value of a, b
# a = [1, 2, 3]
# b = a
# a[0], a[1], a[2] = 4, 5, 6
# print(a)  # [4, 5, 6]
# print(b)  # [4, 5, 6]