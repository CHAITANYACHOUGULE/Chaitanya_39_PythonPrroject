
d1={1:"Hello",2:"Hieee",3:"Welcome"}

print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get(3))

newd=d1.copy()
print(newd)
print(d1.pop(1))


d2={4:"byeee"}
d1.update(d2)
#d1.update(5, "okyyyy")
print(d1)
d1.clear()
print(d1)