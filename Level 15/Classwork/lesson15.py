x = int(input("Enter a number: "))
for i in range(2, x):
    if x % i == 0:
        print("Number is prime ")
    else:
        print("Number isn't prime ")

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1