def descending_order(num):
    num_str = str(num)
    digits = []
    for x in num_str:            
        digit = int(x)
        digits.append(digit)
    sorted_digits = sorted(digits, reverse=True)
    return int("".join(map(str, sorted_digits)))