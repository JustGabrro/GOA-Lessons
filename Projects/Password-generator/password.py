import random
import string

def generate_password(length=8, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    while True:
        try:
            length = int(input("შეიყვანეთ პაროლის სიგრძე: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    use_letters = input("შეიცავდეს ასოებს (y/n)? ").lower() == 'y'
    use_digits = input("შეიცავდეს ციფრებს (y/n)? ").lower() == 'y'
    use_symbols = input("შეიცავდეს სიმბოლოებს (y/n)? ").lower() == 'y'
    
    password = generate_password(length, use_letters, use_digits, use_symbols)
    print("Generated Password:", password)
