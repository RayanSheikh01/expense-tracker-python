import pandas as pd
import matplotlib.pyplot as plt

# parse_dates allows the dates to be treated as dates
expense_history = pd.read_csv('expense_history.csv', parse_dates=['date'])

# start and end date of statement
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
    plt.plot(dates, prices)
    plt.show()



# start_date = "2022-01-01"
# end_date = "2022-01-31"

# after_start_date = dates[1] >= start_date
# before_end_date = dates[2] <= end_date
# print(expense_history.loc[after_start_date&before_end_date])

