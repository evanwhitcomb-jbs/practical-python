# bounce.py
#
# Exercise 1.5
height = 100
bounce = 3 / 5
count = 0

while count < 10:
    height = height * bounce
    count = count + 1
    print(count, round(height, ndigits=4))
