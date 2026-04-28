data = input("Enter your data :")

try:
    int(data)
    print(f"Type: int")
except ValueError:
    try:
        float(data)
        print(f"Type: float")
    except ValueError:
        if data.lower() in ("true", "false"):
            print(f"Type: bool")
        else:
            print(f"Type: str")