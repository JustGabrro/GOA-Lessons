# def solution(text, ending):
#     sliced_str = text[len(text) - len(ending):]       #   String ends with?   
#     if sliced_str == ending:
#         return True    
#     return False


# def is_triangle(a, b, c):
#     if(a <= 0):
#         return False
#     elif b <= 0:
#         return False                         #   Is this a triangle?
#     elif c <= 0:
#         return False
#     elif( a + b <= c or a + c <= b or b + c <= a): 
#         return False
#     else:
#         return True


# def number(bus_stops):
#     people = 0
#     for on, off in bus_stops:           #   Number of People in the Bus
#         people += on - off
#     return people


# def reverse_words(text):
#     words_list = text.split(" ")
#     reversed_words = []                     #   Reverse words
#     for i in words_list:
#         reversed_words.append(i[::-1])
#     return " ".join(reversed_words)


# def arithmetic(a, b, operator):
#     operations = {
#         "add": lambda x, y: x + y,
#         "subtract": lambda x, y: x - y,       #   Make a function that does arithmetic!
#         "multiply": lambda x, y: x * y,
#         "divide": lambda x, y: x / y
#     }
#     return operations[operator](a,b)


# def solution(s):
#     result = ""
#     for char in s:    
#         if char.isupper():               #    Break camelCase
#             result += " " + char
#         else:
#             result += char
#     return result


# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True             #   Is a number prime?
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True


# def pyramid(n):
#     result = []
#     for i in range(1, n + 1):       #   Pyramid Array
#         result.append([1] * i)
#     return result