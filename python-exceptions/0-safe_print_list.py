#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            try:
                print(my_list[i], end="")
                printed += 1
            except IndexError:
                break
    except Exception:
        pass
    print()
    return printed
