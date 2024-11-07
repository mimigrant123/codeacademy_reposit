#LOGIN SYSTEM WITH ENDLESS LOOP
# user = "admin"
# pswrd = "3057"
#
# name = input("Enter username: ")
# password = input("Enter password: ")
#
# while user != name and pswrd != password:
#     name = input("Enter username: ")
#     password = input("Enter password: ")
#     if user == name and pswrd == password:
#         break
# print(f"Login successful! Welcome, {user}.")


#SUM AND AVERAGE OF INTEGERS
#
# x = 0
# s = 0
# avrg = 0
#
# for i in range(1,11):
#     x = int(input(f"Enter integer {i}: "))
#     s += x
#
# print(f"Sum: {s}, Average:", s/10)


#PIN CODE CRACKER
# stored_pin = "0234"
# stored_pin = int(stored_pin)
# x = 0
#
# for i in range(0,10000):
#     if x != stored_pin:
#         x += 1
#     else:
#         break
# print(f"{x:04}")

#GENERATE FIBONACCI SEQUENCE

x = 0
y = 1
z = 0
print("Fibonacci sequence: ", x, end=" ")

for i in range(0,9):
    x = y
    y = z
    z = x + y
    print(z, end=" ")

#CALCULATE AVERAGE AND LIST NUMBERS
#
# l = []
# fnsh = "done"
# a = 0
# s = 0
# c = 0
# while a != fnsh:
#     a = input(f"Enter a number (or '{fnsh}' to finish): ")
#     l += a
#     a = int(a)
#     s += a
#     a = str(a)
#     c += 1
#
# print("Numbers:", l)
# print("Average:", s/c)