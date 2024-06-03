def find_maximum_of_4(a, b, c, d):
    """
    ეს ფუნქცია პოულობს 4 ელემენტიდან მაქსიმუმს.

    :a: პირველი ელემენტი
    :b: მეორე ელემენტი
    :c: მესამე ელემენტი
    :d: მეოთხე ელემენტი
    :return: მაქსიმალური მნიშვნელობა 4 ელემენტიდან
    """
    max_val = a 

    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    if d > max_val:
        max_val = d
    
    return max_val

a = 12
b = 4
c = 19
d = 33

max_value = find_maximum_of_4(a, b, c, d)
print(f"Max value: {max_value}")
