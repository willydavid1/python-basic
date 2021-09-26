def converter(currency_type, exchangeRateValue):
    currencyAmount = float(input(f'Amount of {currency_type}: '))
    exchangeValue = round(currencyAmount / exchangeRateValue, 2)
    print(f'You have ${exchangeValue} dollars')

    print(f'-------- {currency_type} to dollars --------')

    USD = float(input('Amount of USD: '))
    exchangeValue = round(USD * exchangeRateValue, 2)
    print(f'You have {exchangeValue} {currency_type}')

menu = """
Welcome =)

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Select an option as a number: """

option = int(input(menu))

if option == 1:
    converter('COL', 3845)
elif option == 2:
    converter('ARS', 65)
elif option == 3:
    converter('MXN', 24)
else:
    print('You did not select any menu option (1, 2, 3)')
