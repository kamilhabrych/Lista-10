dict1 = {
    'polski': 'angielski',
    'rower': 'bike',
    'samochód': 'car',
    'czerwony': 'red',
}

with open('dictionary.txt', 'w', encoding='UTF8') as f:
    for value, key in dict1.items():
        f.write(value + ': ' + key + '\n')
        
f.close()