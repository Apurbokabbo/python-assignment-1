t = (10, 20, 30, 40, 50)
list = list(t)
print(list[0])
print(list[-1])
print(list[1:3])


list[2] =60
list.append(100)
print(list)
del list[3]
print(list)

t=tuple(list)
print(t)