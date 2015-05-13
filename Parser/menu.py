import sys
sys.path.extend(['/home/gabriel/Materiale/Studiu/Proiecte personale/Python/project_currency'])

from Parser.AllCurrenciesList import AllCurrencyList
from Parser.OneCurrency import OneCurrency


answer = 0
while answer != 5:
    print("Menu")
    print("=====")
    print("1. One currency analyze")
    print("2. List currencies")
    print("3. Find a currency")
    print("4. Find greatest change")
    print("5. Exit")

    answer = int(input("Choose your answer:"))

    if answer == 1:
        OneCurrency().run()

    if answer == 2:
        AllCurrencyList().run()

    if answer == 3:
        AllCurrencyList().filter()

    if answer == 4:
        print("Not implemented")

    if answer == 5:
        break

print("By by")