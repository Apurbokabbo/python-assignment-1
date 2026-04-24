char = input("Enter a character: ").lower()

match char:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"'{char}' is a Vowel")
    case _ if char.isdigit():
        print(f"'{char}' is a Digit")
    case _ if char.isalpha():
        print(f"'{char}' is a Consonant")
    case _:
        print("Invalid character!")