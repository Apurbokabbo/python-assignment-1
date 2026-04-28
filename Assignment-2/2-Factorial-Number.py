def factorial(num):
    if  num < 0:
        return 0

    if num == 0 or num == 1:
        return 1

    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

num_list =[-10,0, 1, 5, 10, 20,-30]

for num in num_list:
    if(factorial(num) ==0):
        print("Number is less than 0")
    else:
        print(f"{num}! = {factorial(num)}")
