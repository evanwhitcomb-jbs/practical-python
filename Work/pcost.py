# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares * price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += price * shares
            except ValueError:
                print("Couldn't parse", row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
