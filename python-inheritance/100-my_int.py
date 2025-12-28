#!/usr/bin/python3
"""class vasitesiyle beraberliyi qeyri beraber edecik :) """


class MyInt(int):
    """ now we willl swap equal and not equals"""

    def equal(self, other):
        return super().__ne__(other)

    def notequal(self, other):
        return super().__eq__(other)
