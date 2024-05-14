# def find_smallest_int(arr):
#     smallest_int = arr[0]

#     for num in arr:
#         if smallest_int > num:                #   Find the smallest integer in the array
#             smallest_int = num
#     return smallest_int


# def no_space(x):
#     result = ""
    
#     for char in x:
#         if char != " ":
#             result = result + char            #   Remove string spaces
#     return result


# def boolean_to_string(b):                     #   Convert a boolean to a string
#     return str(b)


# def sum_array(a):
#     sum = 0
    
#     for num in a:                             #   Sum arrays
#         sum += num
#     return sum


# def abbrev_name(name):
#     name = name.upper()
#     splited_name = name.split(" ")            #   Abbreviate a two word name                                           
#     first_name = splited_name[0]
#     last_name = splited_name[1]
    
#     result = first_name[0] + "." + last_name[0]
#     return result


# def maps(a):
#     doubled_numbers = []
#     for num in a:
#         doubled_numbers.append(num * 2)       #   Beginner - Lost Without a Map

#     return doubled_numbers


# def make_upper_case(s):
#     s = s.upper()                             #   MakeUpperCase
#     return s


# def find_average(numbers):
#     if numbers == []:
#         return 0                              #   Calculate average

    
#     return sum(numbers) / len(numbers)


# def bmi(weight, height):
#     bmi_mass = weight / (height ** 2)
#     if bmi_mass <= 18.5:
#         return "Underweight"
#     elif bmi_mass <= 25.0:                    #   Calculate BMI
#         return "Normal"
#     elif bmi_mass <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"