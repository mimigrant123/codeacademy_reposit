"""Exercise 3: Log File Analysis
Objective: Handle structured text files and perform complex data extraction.
Create a log file named server.log with the following content:
2024-12-01 12:00:01 INFO User logged in: user123
2024-12-01 12:05:23 ERROR Failed to load resource: /images/banner.png
2024-12-01 12:15:45 INFO User logged out: user123
2024-12-01 13:00:01 INFO User logged in: user456
2024-12-01 13:05:23 ERROR Failed to load resource: /css/styles.css

Write a Python program to:
Parse the log file and extract all lines containing the keyword ERROR.
Save these lines into a new file named error.log.
Count the total number of INFO and ERROR entries in the original file and display the results:
INFO entries: 3
ERROR entries: 2"""

with open("server.log", "r") as f:
    lines = f.readlines()
error_log = []
for line in lines:
    if "ERROR" in line:
        error_log.append(line)
print(error_log)

with open("error.log", "w") as f:
    f.writelines(error_log)

with open("server.log", "r") as f:
    lines = f.readlines()
error_counter = 0
info_counter = 0
for line in lines:
    if "ERROR" in line:
        error_counter += 1
    if "INFO" in line:
        info_counter += 1
print(error_counter)
print(info_counter)