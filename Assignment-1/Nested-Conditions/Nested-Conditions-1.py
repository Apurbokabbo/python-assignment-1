num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
num_3 = int(input("Enter another number: "))

if num_1>num_2:
    if num_1>num_3:
        print("Your Entered Largest Number is :",num_1)
elif num_2>num_1:
    if num_2>num_3:
        print("Your Entered Largest Number is :",num_2)

elif num_3>num_1:
    if num_3>num_2:
        print("Your Entered Largest Number is :",num_3)

else:
    print("All Number Are Equal")
