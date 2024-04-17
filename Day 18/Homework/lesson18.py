# def filter_numbers(numbers):
#     filtered_numbers = []
#     for num in numbers:
#         if num % 4 == 0:
#             filtered_numbers.append(num)
#     return filtered_numbers
# print(filter_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))


# def add_name():
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     name_list = [first_name, last_name]
#     return name_list

# result = add_name()
# print(result)



# def filter_list(start_num,end_num):
#     filtered_list = []
    
#     for i in range(start_num,end_num):
#         if i % 2 == 0:
#             filtered_list.append(i ** 2)
#         else:
#             filtered_list.append(i ** 0.5)
#     return filtered_list

# start_num = int(input("Enter first number: "))
# end_num = int(input("Enter second password: "))
# result_list = filter_list(start_num,end_num)
# print(result_list)



# def last_name(surname):
#     word_list = []
#     even_index_list = []
#     for i in surname:
#         word_list.append(i)
#     for x in range(len(word_list)):
#         if x % 2 == 0:
#             even_index_list.append(word_list[x])
#     return even_index_list
# print(last_name("Jakhveladze"))