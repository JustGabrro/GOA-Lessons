# def variance(numbers): 
#     result = sum(numbers) / len(numbers)      #   Calculate Variance
#     x_diff = []
#     for y in numbers:
#         diff = y - result
#         x_diff.append(diff ** 2)
#     sum_x_diff = sum(x_diff)
#     variance = sum_x_diff / len(numbers)
    
#     return variance


# def generate_hashtag(s):
#     if s == "":
#         return False
#     else:
#         word = ""
#         splited_s = s.split()      #   The Hashtag Generator
#         for i in splited_s:
#             a = i.capitalize()
#             word += a
#         if len(word) >= 140:
#             return False
#         else:
#             return f"#{word}"