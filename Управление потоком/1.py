def deliter(number):
    list = []

    for i in range(1, number + 1):
        if number % i == 0:
            list.append(i)

    return list

print(deliter(50))