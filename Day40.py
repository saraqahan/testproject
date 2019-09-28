list = [-4,-6,-5,-1,2,3,7,9,88]
print(list)
f = lambda y : y
for y in list:
    if (f(y)) < 0:
        list.remove(f(y))
        print(list)
for y in list:
    if (f(y)) < 0:
        list.remove(f(y))
        print(list)
for y in list:
    if (f(y)) < 0:
        list.remove(f(y))
        print(list)
