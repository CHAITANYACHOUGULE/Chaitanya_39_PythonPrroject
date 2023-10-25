l1=[1,2,"Byeee",3.5]
print(type(l1),l1)

print(l1[0 :])

print(l1[:])

print(l1[2:4])

print(l1[ :4])

print(l1[1:4:2])

print(l1[-1])

print(l1[-3:-1])

l1[2]=10
print(l1)

l1[2:4]=[5,23]
print(l1)

#reptition

l2=l1*2
print(l2)

#concenation
l3=l1+l2
print(l3)

#adding elements in list
l4=[]
n=int(input("Enter the no. of elements  "))
for i in range(0,n):
    l4.append(input("Enter element"))
    
for i in l4:
    print(i,end=" ")