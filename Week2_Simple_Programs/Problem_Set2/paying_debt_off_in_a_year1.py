monthlyInterestRate = annualInterestRate / 12.0
for _ in range(12):
    minimumPayment = round(balance * monthlyPaymentRate, 2)
    unpaidBalance = balance - minimumPayment
    balance = round(unpaidBalance * (1 + monthlyInterestRate), 2)
print('Remaining balance:', str(balance))
