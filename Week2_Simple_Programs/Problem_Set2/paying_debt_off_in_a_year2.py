monthlyInterestRate = annualInterestRate / 12.0
lowestPayment = 0
remainBalance = balance
while remainBalance > 0:
    lowestPayment += 10
    remainBalance = balance
    for _ in range(12):
        unpaidBalance = remainBalance - lowestPayment
        remainBalance = round(unpaidBalance * (1 + monthlyInterestRate), 2)
print('Lowest Payment:', str(lowestPayment))
