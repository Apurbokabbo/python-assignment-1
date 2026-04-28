text = input("Enter a string: ")
count = 0
for char in text:
    if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
        count += 1


print("Entered String Contain Vowel Count Is :",count)