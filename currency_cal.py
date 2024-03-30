# To calculate the currency
# Assume that the user inputs amounts and currency names with spaces in between, such as '100 dollar,' '1000 yen,' '13 euro,' and '100 yuan'


calculator = {'dollar': 1167,
            'yen': 1.096,
            'euro': 1268,
            'yuan': 171}

user = input("input: ")
money, currency = user.split()
print(float(money) * calculator[currency], "won")

