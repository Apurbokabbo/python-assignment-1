num_1 = int(input("Enter a Number: "))

if num_1 %2 == 0 :
    print(f"{num_1} divided by 2")
    if num_1 % 3 == 0:
        print(f"{num_1} divided by 2 and 3 ")
else:
    print(f"{num_1} not divided by 2")