# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        headers
        for line in f:
            row = line.split(',')
            try:
                shares = float(row[1])
                price = float(row[2])
                total_cost = total_cost + (price * shares)
            except ValueError:
                print("Couldn't parse", line)
    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
