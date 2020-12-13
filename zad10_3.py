def bezpowt(sl):
    if len(sl) == len(set(sl)):
        return 1
    else:
        return 0

sl1 = {
    'Color1': 'Black',
    'Color2': 'White',
    'Color3': 'Green',
    'Color4': 'Red'
}

sl2 = {
    'Animal1': 'Dog',
    'Animal2': 'Cat',
    'Animal3': 'Dog',
    'Animal4':'Turtle'
}

l1 = list(sl1.values())
l2 = list(sl2.values())

print(bezpowt(l1))
print(bezpowt(l2))