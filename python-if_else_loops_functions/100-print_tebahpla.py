#!/usr/bin/python3
for i in range(65, 91):
    if i % 2 != 0:
        alphabet = chr(187 - i)
    else:
        alphabet = chr(155 - i)
    print("{}".format(alphabet), end="")
