import math
import re

#User Information to Dictionary
# a = input("Enter your name: ")
# b = input("Enter your surname: ")
# c = int(input("Enter your age: "))
# my_dict = {"name" : a, "surname" : b, "age" : c}
# print(my_dict)

#Set for Uniqueness
# a = input("Enter a student's name (or type 'done' to finish): ")
# l = []
# l.append(a)
# while a != "done":
#     a = input("Enter a student's name (or type 'done' to finish): ")
#     l.append(a)
# l.remove(l[-1])
# s = set(l)
# print(f"List of students going on the trip: {s}")


#Word dictionary
# FINISH IT!!!
# a = input("Enter a word to look up its meaning (or 'done' to finish): ")
# b = input(f"The meaning of {a} is: ")
# k = []
# v = []
# k.append(a)
# v.append(b)
# while a != "done":
#     a = input("Enter a word to look up its meaning (or 'done' to finish): ")
#     if a == "done":
#         break
#     b = input(f"The meaning of {a} is: ")
#     k.append(a)
#     v.append(b)
# dictionary = dict(zip(k, v))
# print(dictionary)


# Phone Book
# names = []
# phones = []
#
# enter = input("Enter the command (Add, Search, Delete or Exit): ")
# while enter != "Exit":
#     if enter == "Add":
#         name = input("Enter a name: ")
#         names.append(name)
#         phone = input("Enter a phone number: ")
#         phones.append(phone)
#         contacts = dict(zip(names, phones))
#         enter = input("Enter the command (Add, Search, Delete or Exit): ")
#     elif enter == "Search":
#         name = input("Enter a name: ")
#         if name in contacts:
#             print(f"{name} : {contacts.get(name)}")
#         enter = input("Enter the command (Add, Search, Delete or Exit): ")
#     elif enter == "Delete":
#         name = input("Enter a name: ")
#         if name in names:
#             del contacts[name]
#         else:
#             print(f"The {name} name is not founded.")
#         enter = input("Enter the command (Add, Search, Delete or Exit): ")
#     elif enter == "Exit":
#         break
#
# print(contacts)


# Manage Student Grades
# names = []
# grades = []
# bul = True
# average = 0
# while bul == True:
#     name = input("Enter student name (or type 'done' to finish): ")
#     if name == "done":
#         break
#     grade = int(input("Enter grade: "))
#     if grade >= 80:
#         names.append(name)
#         grades.append(grade)
#         dictionary = dict(zip(names, grades))
#
# average = round(sum(grades) / len(grades), 2)
# print(f"Average of all students: {average}")
#
# while bul == True:
#     name = input("Enter a student name to check (or type 'done' to finish): ")
#     if name == "done":
#         break
#     if name in dictionary:
#         print(f"{name} was found. Grade: {dictionary.get(name)}")
#     if name not in dictionary:
#         print(f"{name} not found.")

# Word Frequency Analyzer
# text = "Hello, how how how are you? How's everything? Hello again!"
# text = text.lower()
# words = re.split(r"[,.?!' ]", text)
# counts = []
# while "" in words:
#     words.remove("")
# count = 0
# print(words)
# for word in words:
#     count = words.count(word)
#     counts.append(count)
# print(counts)
# dictionary = dict(zip(words, counts))
# print(dictionary)