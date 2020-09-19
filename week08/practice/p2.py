old_list = [i for i in range(11)]

new_list1 = old_list
new_list2 = list(old_list)

new_list3 = old_list[:]

old_list.append([11, 12])

# print(old_list)
# print(new_list1)
# print(new_list2)
# print(new_list3)

import copy
new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)
old_list[11][0] = 13
print(old_list)
print(new_list4)
print(new_list5)