def primeNumberIdentifier (number):
    if number < 2:
        return False
    if number < 4:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


number = [1, 2, 3, 4,13, 17, 18,19, 97, 100]
for num in number:
    if primeNumberIdentifier(num):
        print(f"Number {num} is a Prime Number")
    else:
        print(f"Number {num} is not a Prime Number")