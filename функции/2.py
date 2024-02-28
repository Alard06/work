def count_vowels(str):
    count = 0
    for i in str:
        if i.lower() in 'аеиоуыэюя':
            count += 1

    return count

print(count_vowels('фывывавыроаиывнграимйуцнгваГ'))