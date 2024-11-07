#TUPLE OPERATIONS
# day_temperatures = (22.6, 19.1, 21.3)
# print(len(day_temperatures))


#MAKING A SHOPPING LIST
# shopping_list = ["milk", "eggs", "bread", "butter"]
# print(shopping_list)
# print(shopping_list[0])
#
# c = 0
# for i in range(len(shopping_list)):
#     if shopping_list[i] != "bread":
#         c += 1
#     else:
#         shopping_list.remove("bread")
#         shopping_list.insert(c, "banana")
# print(shopping_list)
#
# shopping_list.insert(0, "apple")
# print(shopping_list)
# shopping_list.append("flour")
# shopping_list.append("sugar")
# print(shopping_list)
# print(shopping_list[2:4])


#HALF TRIANGLE
# count = int(input("Enter the triangle size: "))
#
# for i in range(1, count + 1):
#     for j in range(1, count + 1):
#         print(j, end= " ")
#         if j == i:
#             print()
#             break


#PRIME NUMBERS IN A RANGE
# list = []
# l = []
# start = int(input("Enter the start of the range: "))
# endlist = int(input("Enter the end of the list: "))
# for i in range(start, endlist + 1):
#     list.append(start)
#     start += 1
# print(len(list))

# for i in range(0, endlist):
#     c = 0
#     if list[i] == 1:
#         continue
#     for j in range(1, 10):
#
#         if list[i] % j == 0:
#             c += 1
#
#     if c < 3:
#         l.append(list[i])
# print(l)


#Longest Consecutive Sequence
# l = list(map(int,input("Enter integers separated with spaces: ").strip().split()))
# print(len(l))
# c = 1
# for i in range(0, len(l) - 1):
#     if l[i] + 1 == l[i+1]:
#         c += 1
# print(c)


#Unique Elements
# a = input("Enter an integer (or 'done' to finish): ")
# l = []
# l.append(a)
# while a != "done":
#     a = input("Enter an integer (or 'done' to finish): ")
#     l.append(a)
# l.remove(l[len(l) - 1])
# list_to_set = set(l)
# print(list_to_set)


