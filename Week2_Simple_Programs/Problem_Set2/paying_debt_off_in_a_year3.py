monthlyInterestRate = annualInterestRate / 12.0
low = balance / 12
high = balance * (1 + monthlyInterestRate) ** 12 / 12
remainBalance = balance
while abs(remainBalance) > 0.1:
    mid = round((low + high) / 2, 2)
    remainBalance = balance
    for _ in range(12):
        unpaidBalance = remainBalance - mid
        remainBalance = round(unpaidBalance * (1 + monthlyInterestRate), 2)
    if remainBalance > 0:
        low = mid
    else:
        high = mid
print('Lowest Payment:', str(mid))
