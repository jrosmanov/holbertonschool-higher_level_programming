#!/usr/bin/python3
def add_touple(touple_a=(), touple_b=()):
    a1 = touple_a[0] if len(touple_a) > 0 else 0
    a2 = touple_a[1] if len(touple_a) > 1 else 0
    b1 = touple_b[0] if len(touple_b) > 1 else 0
    b2 = touple_b[1] if len(touple_b) > 1 else 0
    return (a1+b1, a2+b2)
