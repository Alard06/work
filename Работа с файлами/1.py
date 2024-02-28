with open('1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    counter = 0
    for line in lines:
        line = line.split()
        counter += len(line)

print(counter)