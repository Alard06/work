def list_duplicate(my_list):
    arr = []
    for i in my_list:
        if i not in arr:
            arr.append(i)

    return arr

def list_duplicate2(my_list):
    my_list = set(my_list)
    return list(my_list)

print(list_duplicate([1,2,2,2,2,3,4,5,6,1]))
print(list_duplicate2([1,2,2,2,2,3,4,5,6,1]))