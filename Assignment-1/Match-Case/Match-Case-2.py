def day_name(day):
    match day:
        case 1:
            return "Saturday"
        case 2:
            return "Sunday"
        case 3:
            return "Monday"
        case 4:
            return "Thursday"
        case 5:
            return "Wednesday"
        case 6:
            return "Thursday"
        case 7:
            return "Friday"
        case _:
            return "Invalid Day"

print(day_name(3))
print(day_name(1))
print(day_name(7))
print(day_name(10))