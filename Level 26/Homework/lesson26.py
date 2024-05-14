""" 1. Manual Sum Function: Create a function called manual_sum that 
iterates over list and adds their sum in a variable, then returns variable. 
Use for loop for this task. """

# def manual_sum(number_list, starting_value = 0):
#     result = starting_value
#     for num in number_list:
#         result += num
#     return result
# print(manual_sum([1,2,3,4,5]))

""" 2. Manual Max Function: Define a function named manual_max that iterates 
through list, updating a variable with the maximum value, 
then returns the maximum value found. Use for loop for this task. """

# def manual_max(num_list):
#     max_value = num_list[0]
#     for num in num_list:
#         if num > max_value:
#             max_value = num
#     return max_value
# print(manual_max([1,2,3,4,100,5]))

""" 3. Manual Min Function: Define a function named manual_min that iterates 
through list, updating a variable with the minimum value, 
then returns the minimum value found. Use for loop for this task. """

# def manual_min(num_list):
#     min_value = num_list[0]
#     for num in num_list:
#         if num < min_value:
#             min_value = num
#     return min_value
# print(manual_min([0,1,2,3,4,5,-100]))

""" 4. Manual Len Function: Develop a function named manual_len that iterates 
through list, counting each element, and returns the count as the length of 
the list. Use for loop for this task. """

# def manual_len(len_list):
#     count = 0
#     for _ in len_list:
#         count += 1
#     return count
# print(manual_len([1,0,0,1,1]))

""" 5. Copy function of reduce: define a function named manual_reduce that 
takes a list as input, then create an empty list named copied_list 
to store the copied items inside it. Then use for loop to loop over each 
item in the original list, append them to the copied_iterable list. In the end, 
return the copied_iterable after iterating through all items. finally demonstrate
 the usage of the manual_reduce function by creating an 
original list, making a copy of it, and printing both the original and copied 
lists. """

# def manual_reduce(num):
#     copied_list = []
#     for i in num:
#         copied_list.append(i)
#     return copied_list, num

# print(manual_reduce([5,10,15,20]))