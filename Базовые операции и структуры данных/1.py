def natural_sort_key(list):
    return [x for x in list if x % 2 == 0]


print(natural_sort_key([1,2,3,4,5,6,7,8,9,10]))