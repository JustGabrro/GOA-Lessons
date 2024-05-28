def count_capital_letters(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count
text = input("Enter a text:")
print(count_capital_letters(text))