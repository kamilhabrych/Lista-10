t1 = (1, 2, 3, 4, 5)
t2 = ('a', 'b', 'c', 'd', 'e')

print(t1)
print(t2)

l = list(t1)
l[0] = 0
del t1
t1 = tuple(l)

print()
print(t1)
print(t2) 