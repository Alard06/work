def optimal_sparkle(c1, b1):
    sparkling_hours = 0
    remaining_fires = c1

    while remaining_fires >= 1:
        sparkling_hours += 2
        remaining_fires -= 1
        if remaining_fires > 0:
            sparkling_hours += (2 * b1)

    return sparkling_hours

c1 = int(input("Введите количество имеющихся у Игоря бенгальских огоньков (с1): "))
b1 = int(input("Сколько потухших бенгальских огоньков можно создать из одного огонька (b1): "))

sparkling_hours = optimal_sparkle(c1, b1)

print("Если Игорь будет действовать оптимально, его огонек будет гореть ", sparkling_hours, " часов.")