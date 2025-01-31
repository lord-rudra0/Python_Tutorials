li=[]

while(True):
    n= int(input("Enter the elements: "))
    li.append(n)
    ch=input("do u want to continue(y/n): ")
    if ch =="n":
        break
    
print(li)
print("Minimum of List is :",min(li))
print("Minimum of List is :",max(li))
