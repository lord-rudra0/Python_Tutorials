investment = int(input("Enter investment: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter  time period: "))
simple_interest = (investment * rate * time) / 100
print("Simple interest is: ", simple_interest)

compound_interest = investment * (pow((1 + rate / 100), time))
compound_interest = compound_interest - investment
print("Compound interest is: ", compound_interest)
print("Total amount after interest: ", investment + compound_interest)


