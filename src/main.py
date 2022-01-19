from tkinter import Tcl, TclError
import pandas as pd
import matplotlib.pyplot as plt

# parse_dates allows the dates to be treated as dates
expense_history = pd.read_csv('expense_history.csv', parse_dates=['date'])

def addExpense(date, name, price):
    expense_history.loc[len(expense_history.index)+1, :] = {
                            'date': date,
                            'name': name,
                            'price': price}
    expense_history.to_csv('expense_history.csv')

# start and end date of statement

def checkExpenses():
    start_date = str(input("Enter the start date of the statement (inclusive, format=yyyy-mm-dd): "))
    end_date = str(input("Enter the end date of the statement (inclusive, format=yyyy-mm-dd): "))

    # to get statemnt to be between start date and end date (inclusive)
    mask = (expense_history['date'] >= start_date) & (expense_history['date'] <= end_date)


    # convert current date format to datetime so that it can be plotted 
    # get date and price from data as the name is not required for graph
    expense_history['date'] = expense_history['date'].dt.date
    data = expense_history.loc[mask, ['date', 'price']]
    dates = []
    prices = []

    # get each date into dates so it can be used as x_axis data
    for date in data['date']:
        # date = re.search('\d+-\d+', str(date)).group(0)
        dates.append(date)

    # get each price into priecs so it can be used as y_axis data
    for price in data['price']:
        prices.append(price)


    # print(points)
    if len(dates) > 0:
        try:
            plt.plot(dates, prices)
            plt.show()
        except TclError:
            pass


def menu():
    print("What would you like to do: ")
    print("1) Add expense")
    print("2) Get expenses from two date intervals")
    print("3) Quit")
    choice = int(input())
    if choice == 1:
        date = str(input("What date did this expense happen: (dd/mm/yy)"))
        name = str(input("What is the name of the item/service you paid for: "))
        price = str(input("What is the price you paid for the service/item (): "))
        if "." not in price:
            price += ".00"
        addExpense(date, name, price)
        print("Successfuly added expense\n")
        menu()
    elif choice == 2:
        checkExpenses()
        menu()
    elif choice == 3:
        quit()

if __name__ == "__main__":
    menu()

    
