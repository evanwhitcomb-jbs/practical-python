# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            try:
                shares = float(row[1])
                price = float(row[2])
                total_cost = total_cost + (price * shares)
            except ValueError:
                print("Couldn't parse", row)
    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
