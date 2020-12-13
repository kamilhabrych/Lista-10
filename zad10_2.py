l1 = ['First Name', 'Last Name', 'Age', 'Birthday']
l2 = ['Kamil', 'Habrych', '22', '24-08-1998']

_dict = {}

for key in l1:
    for value in l2:
        _dict[key] = value
        l2.remove(value)
        break

print(_dict)