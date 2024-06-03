def find_maximum_of_5(a, b, c, d, e):
    """
    ეს ფუნქცია პოულობს 5 ელემენტიდან მაქსიმუმს.

    :a: პირველი ელემენტი
    :b: მეორე ელემენტი
    :c: მესამე ელემენტი
    :d: მეოთხე ელემენტი
    :e: მეხუთე ელემენტი
    :return: მაქსიმალური მნიშვნელობა 5 ელემენტიდან
    """
    max_val = a 

    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    if d > max_val:
        max_val = d
    if e > max_val:
        max_val = e
    
    return max_val

a = 12
b = 4
c = 19
d = 33
e = 5

max_value = find_maximum_of_5(a, b, c, d, e)
print(f"Max value: {max_value}")
