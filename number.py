f=open('number.txt','r')
f1=open('even.txt','w')
f2=open('odd.txt','w')

s = f.read()
num1=s.split()
a= len(num1)
for i in range (a):
    num=int(num1[i])
    if (num % 2==0):
        f1=open('even.txt','a')
        str1=str(num)+","
        f1.write(str1)
    else:
     f2=open('odd.txt','a')
     str2=str(num)+","
     f2.write(str2)





f.close()