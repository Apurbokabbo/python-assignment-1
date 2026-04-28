number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"Divisible by both 3 and 5: {number}")
elif number % 3 == 0:
    print(f"Divisible by 3 but not 5: {number}")
elif number % 5 == 0:
    print(f"Divisible by 5 but not 3: {number}")
else:
    print(f"Not divisible by 3 or 5: {number}")