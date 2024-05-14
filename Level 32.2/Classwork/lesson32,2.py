# def validate_pin(pin):
#     if pin.isdigit():
#         if len(pin) == 4 or len(pin) == 6:       #    Regex validate PIN code
#             return True
#         else:
#             return False
#     else:
#         return False    
#     return pin


# def open_or_senior(data):
#     result = []
#     for _ in data:
#         age = _[0]                       #    Categorize New Member
#         handicap = _[1]
#         if age >= 55 and handicap > 7:
#             result.append("Senior")
#         else:
#             result.append("Open")
#     return result


# def min_max(lst):
#     return [min(lst), max(lst)]        #    The highest profit wins!


# def arithmetic(a, b, operator):
#     if operator == "add":
#         return a + b
#     elif operator == "subtract":     #  Make a function that does arithmetic!
#         return a - b  
#     elif operator == "multiply":
#         return a * b
#     elif operator == "divide":
#         return a / b
    
#     return operator


# def capitals(word):
#     letters = []
#     for index in range(len(word)):    #   Find the capitals
#         if word[index].isupper():
#             letters.append(index)
#     return letters


# def array_diff(a, b):
#     result = []            #   Array.diff
#     for x in a:
#         if x not in b:
#             result.append(x)
#     return result


# def to_weird_case(words):
#     result = []
#     for word in words.split():
#         symbol = ""
#         index = 0
#         for char in word:             #  WeIrD StRiNg CaSe
#             if index % 2 == 0:
#                 symbol += char.upper()
#             else:
#                 symbol += char.lower()
#             index += 1
#         result.append(symbol)
#     return " ".join(result)


# def camel_case(s):
#     words = s.split()
#     camel_case = ""           #   CamelCase Method
#     for word in words:
#         camel_case += word.capitalize()
#     return camel_case


# def kebabize(s):
#     kebab_case = ""
#     for char in s:
#         if char.isupper():        
#             if kebab_case and kebab_case[-1] != "-":      #   Kebabize
#                 kebab_case += "-"
#             kebab_case += char.lower()
#         elif char.isalpha():
#             kebab_case += char
#     return kebab_case

