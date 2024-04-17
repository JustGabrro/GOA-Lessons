# def sum_two_smallest_numbers(numbers):            #   Sum of two lowest positive integers
#     numbers.sort()
#     return numbers[0] + numbers[1]



# def friend(x):
#     friends = []
#     for name in x:                                #   Friend or Foe?
#         if len(name) == 4:
#             friends.append(name)
#     return friends



# def find_short(s):
#     words_list = s.split(" ")
#     min_length = len(words_list[0])               #   Shortest Word
#     for word in words_list:
#         if min_length > len(word):
#             min_length = len(word)
#     return min_length



# def get_middle(s):
#     word_length = len(s)
#     index = word_length // 2                      #   Get the Middle Character
#     if word_length % 2 == 0:
#         return s[index - 1] + s[index]
#     return s[index]



# def high_and_low(numbers):
#     string_list = numbers.split(" ")              #   Highest and Lowest
#     numbers_list = []
#     for number in string_list:
#         numbers_list.append(int(number))
#     print(numbers_list)
#     return str(max(numbers_list)) + " " + str(min(numbers_list))