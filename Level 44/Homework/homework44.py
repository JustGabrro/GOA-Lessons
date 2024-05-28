# 1.1.3 EXERCISES

# def count_capital_letters(text):
#     count = 0
#     for char in text:
#         if char.isupper():
#             count += 1
#     return count
# text = input("Enter a text:")
# print(count_capital_letters(text))

###############################################

# def calculate_average(number_strings):
#     total = 0
#     count = 0
#     for number_str in number_strings:
#         number = float(number_str)
#         total += number
#         count += 1
#     return total / count if count > 0 else 0

# number_strings = ["1.5", "2.5", "3.5"]
# print(calculate_average(number_strings))

###############################################

# def are_distinct(a, b, c):
#     if a == b:
#         return False
#     elif a == c:
#         return False
#     elif b == c:
#         return False
#     else:
#         return True

# a, b, c = 1, 2, 3
# print(are_distinct(a, b, c))

###############################################

# def find_largest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# a, b, c = 1, 2, 3
# print(find_largest(a, b, c))

###############################################

# def find_second_largest(lst):
#     if len(lst) < 2:
#         return None
#     first, second = float('-inf'), float('-inf')
#     for number in lst:
#         if number > first:
#             second = first
#             first = number
#         elif number > second and number != first:
#             second = number
#     return second

# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(find_second_largest(lst))

