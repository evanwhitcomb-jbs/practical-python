# report.py
#
# Exercise 2.4
import sys
import csv

def read_portfolio(filename):
    '''Reads portfolio file into tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            portfolio.append(holding)
    
    return portfolio