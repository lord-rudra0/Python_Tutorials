old_list=[]
while (True):
    n=int(input("Enter the Element : "))
    old_list.append(n)
    ch=input("Do u Want to Enter Next element(y/n): ")
    if ch=="n":
        break
    
print(old_list)

even=[]

for i in range(len(old_list)):
    if old_list[i]%2==0:
        even.append(old_list[i])
print(even)