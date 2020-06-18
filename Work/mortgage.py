# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    if payment > principal:
        payment = principal
        principal = 0
        total_paid = total_paid + payment
    elif month in range(extra_payment_start_month, extra_payment_end_month):
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    print(month, round(total_paid, ndigits=2), round(principal, ndigits=2))

print('Total paid', round(total_paid, ndigits=2))
print('Number of months', month)
