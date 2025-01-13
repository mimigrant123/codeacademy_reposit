"""Exercise 2: Counting Words in a File (Intermediate)
Objective: Practice reading files and processing text data.
Download or create a file named sample.txt containing at least a few paragraphs of text.
Write a Python program to:
Open the file and read its content.
Count the total number of words in the file.
Count how many times the word "Python" (case-insensitive) appears in the file.
Print the results in this format:
Total Words: 123 Occurrences of 'Python': 5"""

with open("sample.txt", "r") as f:
    lines = f.readlines()
    count_text = 0
    count_exact_word = 0
    for line in lines:
        words = line.split()
        count_text += len(words)
        words = list(map(lambda x: x.lower(), words))
        for word in words:
            if word == "python":
                count_exact_word += 1
    print(f"Total words: {count_text}. Occurrences of 'Python': {count_exact_word}")





