master=[]
while (True):
    n=int(input("Enter the Element : "))
    master.append(n)
    ch=input("Do u Want to Enter Next element(y/n): ")
    if ch=="n":
        break
    
print(master)

list2=[]

key=int(input("enter the Key :"))

for i in range(len(master)):
    if master[i]<key:
        list2.append(master[i])
print(list2)