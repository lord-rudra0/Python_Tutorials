import functools

li=[]

while (True):
    n=int(input("Enter the Element : "))
    li.append(n)
    ch=input("Do u Want to Enter Next element(y/n): ")
    if ch=="n":
        break
print(li)
li.sort()
print(li)
print("3rd largest element is: ",li[2])

 
