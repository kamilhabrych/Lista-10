dict1 = {}

with open('dictionary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        (key, value) = line.rstrip("\n").split(':')
        dict1[key] = value

    f.close()

    print(dict1.keys(), dict1.values(), sep="\n")