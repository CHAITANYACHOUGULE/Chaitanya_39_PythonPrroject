import array as arr
a=arr.array('i',[1,2,3])
print("Int array")
for i in range(0,3):
    print(a[i],end=" ")
    
a1=arr.array('d',[2.5,3.5,4.5])
print("\nFloat array")
for i in range(0,3):
    print(a1[i],end=" ")

    
a1.append(25);
print(a1)
#insert in int array
a.insert(1, 5)
print("\n",a)



