# pcost.py
#
# Exercise 1.27

total_cost = 0.0

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
headers
for line in f:
    row = line.split(',')
    shares = float(row[1])
    price = float(row[2])
    total_cost = total_cost + (price * shares)

f.close()

print(f'Total cost {total_cost}')
