"""Exercise 1: Reading a CSV File
Goal: Understand the basics of reading a CSV file.
Write a Python script that reads a CSV file called students.csv with the following structure:
Name, Age, Grade
Alice, 20, 85
Bob, 22, 90
Charlie, 19, 78
Parse the file line by line.
Print the contents of the file in the format:
Name: Alice, Age: 20, Grade: 85"""

name_row = []
age_row = []
grade_row = []

with open("students.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        data_row = line.split(",")
        # filtered = line.replace("\n", "")
        name_row.append(data_row[0])
        age_row.append(data_row[1])
        grade_row.append(data_row[2])
        # print(data_row[2])
    # for line in grade_row:
    #     filtered = line.replace("\n"," ")
    for i in range(1, len(name_row)):
        print(f"{name_row[0]}: {name_row[i]},{age_row[0]}:{age_row[i]}, Grade:{grade_row[i]}")

