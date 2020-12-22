dict1 = {}

with open('dictionary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        (key, val) = line.rstrip("\n").split(':')
        dict1[key] = val

    f.close()

    print(dict1.keys(), dict1.values(), sep="\n")