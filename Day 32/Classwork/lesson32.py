# def solution(s):
#     new_str = ""
#     for i in s:
#         if i.isupper():
#             new_str += " " + i
#         else:
#             new_str += i
#     return new_str


# def is_prime(num):
#     counter = 0
#     for i in range(1, num + 1):           #   1
#         if num % i == 0:
#             counter += 1
#     if counter != 2:
#         return False
#     return True


# def pyramid(n):
#     new_list = []
#     for i in range(1, n + 1):             #   2
#         new_list.append(i * [1])
#     return new_list


# def reverse(st):
#     new_list = []
#     splited_str = st.split()              
#     for i in splited_str[::-1]:
#         new_list.append(i)
#     return " ".join(new_list)


