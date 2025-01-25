BinNum=input("Enter The Binary Number: ")
n=len(BinNum)
# print(n)
num=0
for i in range(n):
    digit=int(BinNum[n-i-1])
    # print(digit)
    num=num+(2**i)*digit
print("Decimal value is :",num)