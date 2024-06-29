# def vaporcode(s):
#     s = s.replace(" ", "")
#     s = s.upper()
#     chars = []
    
#     for char in s:
#         chars.append(char)
    
#     return "  ".join(chars)

###########################################

# def length_of_sequence(arr,n):
#     if arr.count(n) != 2:
#         return 0
    
#     first = arr.index(n)
#     second = arr.index(n, first + 1)
    
#     return second - first + 1

###########################################

# def tail_swap(strings):
#     first_arr = strings[0].split(':')
#     second_arr = strings[1].split(':')
    
    
#     temp = first_arr[1]
#     first_arr[1] = second_arr[1]
#     second_arr[1] = temp
    
    
#     return [":".join(first_arr), ":".join(second_arr)]

###########################################

def reverse_alternate(st):
    words = st.split()
    res = []
    for i in range(len(words)):
        if i % 2 == 1:
            res.append(words[i][::-1])
        else:
            res.append(words[i])
    return " ".join(res)