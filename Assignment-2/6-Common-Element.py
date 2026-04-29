def common_elements(lst1, lst2):
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)

    i = j = 0
    result = []

    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            result.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] < lst2[j]:
            i += 1
        else:
            j += 1

    return result


list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_2 = [2,3,4,5,6,7,8,9,20]

print(common_elements(list_1, list_2))