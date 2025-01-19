
income = int(input("Enter the income: "))
tax = 0
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 0.05 * (income - 250000)
elif income <= 750000:
    tax = 0.10 * (income - 500000) + 12500
elif income <= 1000000:
    tax = 0.15 * (income - 750000) + 37500
elif income <= 1250000:
    tax = 0.20 * (income - 1000000) + 75000
elif income <= 1500000:
    tax = 0.25 * (income - 1250000) + 125000
else:
    tax = 0.30 * (income - 1500000) + 187500
print("Income tax is: ", tax)
print("Net income is: ", income - tax)




    
    