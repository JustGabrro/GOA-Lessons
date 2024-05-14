# def duplicate_encode(word):      # Duplicate Encoder
#     word = word.lower()
#     result = ""
#     for char in word:
#         if word.count(char) > 1:
#             result += ")"
#         else:
#             result += "("
#     return result


# def is_pangram(st):       # Detect Pangram
#     letters = set()
#     for char in st.lower():
#         if char.isalpha():
#             letters.add(char)
#     return len(letters) == 26


# def name_in_str(strng : str, name : str) -> bool:     # What's A Name In?
#     strng_x = 0
#     name_y = 0
#     strng = strng.lower()
#     name = name.lower()
    
#     while strng_x < len(strng) and name_y < len(name):
#         if strng[strng_x] == name[name_y]:
#             name_y += 1
#         strng_x += 1
#     return name_y == len(name)


# def memesorting(meme):            # Memesorting
#     meme_lower = meme.lower()
#     patterns = {
#         "Roma": "bug",
#         "Maxim": "boom",
#         "Danik": "edits"
#     }
#     for person, pattern in patterns.items():
#         pattern_index = 0
#         for char in meme_lower:
#             if char == pattern[pattern_index]:
#                 pattern_index += 1
#                 if pattern_index == len(pattern):
#                     return person
#     return "Vlad"


# def first_non_repeating_letter(s):        # First non-repeating character
#     s_lower = s.lower()
#     char_count = {}
#     for char in s_lower:
#         char_count[char] = char_count.get(char, 0) + 1
#     for char in s:
#         if char_count[char.lower()] == 1:
#             return char
#     return ""