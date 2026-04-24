age = int(input("Enter your age: "))

if age<5:
    print("You Ticket Is Free.")
elif age>=5:
    if age<=18:
        print("You Ticket Is Discontinued.")
    elif age > 18:
        print("You Ticket Price Is Full.")
