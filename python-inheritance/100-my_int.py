#!/usr/bin/python3
"""class vasitesiyle beraberliyi qeyri beraber edecik :) """


class MyInt(int):
    """class yaratdiq """
    def __equal__(self, other):
        return super().__notequal__(other)

    def __notequal__(self, other):
        return super().__equal__(other)
        