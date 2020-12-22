def odwr(sl):
    if len(sl) == len(set(sl)):
        reverse_dict1 = {value: key for (key, value) in dict1.items()}
        return reverse_dict1
    else:
        error = print("Error! Repetition in directory!")
        return error
  
dict1 = {
    'polski': 'angielski',
    'rower': 'bike',
    'samochód': 'car',
    'czerwony': 'red',
}
 
print(odwr(dict1))