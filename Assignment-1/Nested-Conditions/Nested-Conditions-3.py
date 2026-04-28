email ="admin@gmail.com"
password = "1234"


username = input("Enter your username: ")
i_pass= input("Enter your password: ")

if username == email:
    if password == i_pass:
        print(f"{username} logged in")
    else:
        print("Invalid Password")

else:
    print("Invalid User.")

