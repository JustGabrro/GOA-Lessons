def find_max(n, a):
    i = n - 1
    max = a[i]
    index = i
    for i in range(n-2):
        if max < a[i]:
            max = a[i]
            index = i
    return index

print(find_max(5, [1, 2, 5, 3, 4]))

