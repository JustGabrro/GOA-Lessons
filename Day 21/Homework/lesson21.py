# def grow(arr):
#     sum_arr = 1
#     for num in arr:                   #   Beginner - Reduce but Grow
#         sum_arr = sum_arr * num
#     return sum_arr


# def get_count(sentence):
#     num_vowels = 0
#     vowels = "aeiou"
#     for x in sentence:                  #   Vowel Count
#         if x in vowels:
#             num_vowels += 1
#     return num_vowels


# def square_digits(num):
#     num_str = str(num)
#     result = ""                         #   Square Every Digit
#     for x in num_str:
#         result += str(int(x) ** 2)
#     return int(result)


# def descending_order(num):
#     num_str = str(num)
#     digits = []
#     for x in num_str:                   #   Descending Order
#         digit = int(x)
#         digits.append(digit)
#     sorted_digits = sorted(digits, reverse=True)
#     return int("".join(map(str, sorted_digits)))


# def likes(names):
#     num_likes = len(names)
#     if num_likes == 0:
#         return "no one likes this"
#     elif num_likes == 1:
#         return f"{names[0]} likes this"                         #   Who likes it?
#     elif num_likes == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif num_likes == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {num_likes - 2} others like this"


# def solution(number):
#     result = 0
#     for i in range(number):             #    Multiples of 3 or 5
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result