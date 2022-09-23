change = input('Please input the amount of change you have due, include the two numbers past the decimal. ')

try:
    float(change)
    isFloat = True
except:
    isFloat = False

while (isFloat == False) or (float(change) < 0):
    change = input('Please input the amount of change you have due, include the two numbers past the decimal. ')

    try:
        float(change)
        isFloat = True
    except:
        isFloat = False

if isFloat == True:
    change = float(change)
    cents = round(change * 100)
    amount = 0

    while cents >= 25:
        amount = int((cents / 25) + amount)
        cents = cents % 25
    while cents >= 10:
        amount = int((cents / 10) + amount)
        cents = cents % 10
    while cents >= 5:
        amount = int((cents / 5) + amount)
        cents = cents % 5
    while cents >= 1:
        amount = int((cents / 1) + amount)
        cents = cents % 1
    print(amount, "coins total")
