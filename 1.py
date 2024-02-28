def sorted_lists(list1, list2):
    res = []
    i = len(list1) - 1
    j = len(list2) - 1

    while i >= 0 and j >= 0:
        if list1[i] > list2[j]:
            res.append(list1[i])
            i -= 1
        else:
            res.append(list2[j])

    while i >= 0:
        res.append(list1[i])
        i -= 1

    while j >= 0:
        res.append(list2[j])
        j -= 1

    return res

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = sorted_lists(list1, list2)
print(result)