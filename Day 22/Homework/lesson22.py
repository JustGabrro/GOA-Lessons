#   Disemvowel Trolls   7 kyu
# def disemvowel(string_):
#     vowels = "aeiouAEIOU"
#     result = ""
#     for char in string_:
#         if char not in vowels:
#             result += char
#     return result


#   Create Phone Number  6 kyu
# def create_phone_number(numbers):
#     first_part = "({}{}{})".format(numbers[0], numbers[1], numbers[2])
#     second_part = "{}{}{}".format(numbers[3], numbers[4], numbers[5])
#     third_part = "{}{}{}{}".format(numbers[6], numbers[7], numbers[8], numbers[9])
#     return "{} {}-{}".format(first_part, second_part, third_part)


#   Remove First and Last Character     8 kyu
# def remove_char(s):
#     return s[1:-1]


#   Simple Pig Latin
# def pig_it(text):
#     words = text.split()
#     pig_words = []
#     for x in words:
#         if x.isalpha():
#             pig_word = x[1:] + x[0] + "ay"
#         else:
#             pig_word = x
#         pig_words.append(pig_word)
#     return " ".join(pig_words)