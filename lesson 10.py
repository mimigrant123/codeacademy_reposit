import math

# Numbers Divisible by 6
#
# l = [a for a in range(1, 1001) if a % 6 == 0]
# print(l)



# Find Numbers Containing Nine
# l = [num for num in range(1, 1001) if "9" in str(num)]
# print(l)



# Count Words with “e”
# l = input("Please enter your text: ")
# count = 0
# words = l.split()
# for word in words:
#     if "e" in word:
#         count += 1
# print(count)


# Count Words Longer Than Five Characters
#
# def words_counter(a):
#     words = a.split()
#     count = 0
#     for word in words:
#         if len(word) > 4:
#             count += 1
#     return print(f"Number of words longer than five characters: {count}")
#
# a = input("Please enter your text: ")
# words_counter(a)


# Letter Frequency Dictionary
# text = input("Please enter your text: ")
#
# letter_frequences = {}
# for letter in text:
#     letter_frequences[letter] = text.count(letter)
#     c = text.count(letter)
#
#
# print(letter_frequences)



# Perfect Square Checker
# def perfect_square_root(num):
#     root = math.sqrt(num)
#     # return math.pow(math.sqrt(num), 2) == num
#     return math.ceil(math.sqrt(num)) == math.floor(math.sqrt(num))
# num = int(input("Enter a number: "))
# print(f"Is {num} is a perfect square? {perfect_square_root(num)}")