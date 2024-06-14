def filter_list(start_num,end_num):
    filtered_list = []
    
    for i in range(start_num,end_num):
        if i % 2 == 0:
            filtered_list.append(i ** 2)
        else:
            filtered_list.append(i ** 0.5)
    return filtered_list

start_num = int(input("Enter first number: "))
end_num = int(input("Enter second password: "))
result_list = filter_list(start_num,end_num)
print(result_list)
