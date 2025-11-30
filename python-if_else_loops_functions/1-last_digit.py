#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = number % 10
if number < 0:
    lastnum = -lastnum
print(f"Last digit of {number} is {lastnum}", end='')
if lastnum > 5:
    print(" and is greater than 5")
elif lastnum ==0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
