list1=[]

while (True):
    n=int(input("Enter the Element : "))
    list1.append(n)
    ch=input("Do u Want to Enter Next element(y/n): ")
    if ch=="n":
        break
    
list2=[]
while (True):
    m=int(input("Enter the Element : "))
    list2.append(m)
    ch=input("Do u Want to Enter Next element(y/n): ")
    if ch=="n":
        break
    
list3=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i]==list2[j]:
            list3.append(list1[i])
            
print(list3)