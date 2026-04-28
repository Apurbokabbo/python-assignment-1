while True:
    print("\n--- Menu ---")
    print("1 -> Add")
    print("2 -> Subtract")
    print("3 -> Exit")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)

        case '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        case '3':
            break

        case _:
            print("Invalid choice! Please try again.")