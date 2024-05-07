# 8kyu

# def array_plus_array(arr1,arr2):      # Array plus array
#     return sum(arr1 + arr2)

#--------------------------------------------------------------

# def rps(p1, p2):
#     if p1 == "scissors" and p2 == "paper":
#         return "Player 1 won!"
#     elif p1 == "paper" and p2 == "rock":       # Rock Paper Scissors!
#         return "Player 1 won!"
#     elif p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     elif p1 == p2:
#         return "Draw!"
#     else:
#         return "Player 2 won!"

#--------------------------------------------------------------

# def area_or_perimeter(l , w):
#     if l == w:
#         return l* w             # Area or Perimeter
#     else:
#         return 2 * l + 2 * w

#--------------------------------------------------------------
# 7kyu

# def remove_url_anchor(url):
#     anchor_index = url.find("#")     # Remove anchor from URL
#     if anchor_index != -1:
#         return url[:anchor_index]
#     else:
#         return url

#--------------------------------------------------------------

# # write the function is_anagram
# def is_anagram(test, original):
#     test = test.lower()
#     original = original.lower()    # Anagram Detection
    
#     sorted_test = sorted(test)
#     sorted_original = sorted(original)
    
#     return sorted_test == sorted_original

#--------------------------------------------------------------

# def mygcd(x, y):
#     if y == 0:     # Greatest common divisor
#         return x
#     return mygcd(y, x %y)

#--------------------------------------------------------------
# 6kyu

# def expanded_form(num):
#     num_str = str(num)
    
#     expanded = []         # Write Number in Expanded Form
    
#     for i, digit in enumerate(num_str):
#         if digit != "0":
#             expanded.append(digit + "0" * (len(num_str) - i - 1))
#     return " + ".join(expanded)

#--------------------------------------------------------------

# def data_reverse(data):
#     reversed_segments = []
    
#     for i in range(len(data) // 8, 0, -1):    # Data Reverse
#         segment = data[(i - 1) * 8: i * 8]
#         reversed_segments.extend(segment)
#     return reversed_segments

#--------------------------------------------------------------

# def collatz(n):
#     sequence = [str(n)]
#     while n != 1:
#         if n % 2 == 0:    # Collatz
#             n //= 2
#         else:
#             n = 3 * n + 1
#         sequence.append(str(n))
#     return "->".join(sequence)

#--------------------------------------------------------------

# def is_pangram(s):
#     letters = set()
                        # Detect Pangram
#     for char in s:
#         if char.isalpha():
#             letters.add(char.lower())
#     return len(letters) == 26

#--------------------------------------------------------------

# def kebabize(st):
#     kebab_case = ""
#     for char in st:       
#         if char.isupper():
#             if kebab_case and kebab_case[-1] != "-":   # Kebabize
#                 kebab_case += "-"
#             kebab_case += char.lower()
#         elif char.isalpha():
#             kebab_case += char
#     return kebab_case

#--------------------------------------------------------------
# 5kyu

# def pig_it(text):
#     words = text.split()
#     pig_words = []            # Simple Pig Latin
#     for x in words:
#         if x.isalpha():
#             pig_word = x[1:] + x[0] + "ay"
#         else:
#             pig_word = x
#         pig_words.append(pig_word)
#     return " ".join(pig_words)