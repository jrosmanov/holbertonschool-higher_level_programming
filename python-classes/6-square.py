#!/usr/bin/python3
"""this will define empty square class """


class Square:
    """reprezents empty class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) and x >= 0 for x in value)
        ):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        self.__area = self.__size ** 2
        return self.__area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.__position[1] + 1):
                print()
            for i in range(1, self.__size + 1):
                for k in range(0, self.__position[0]):
                    print(' ', end='')
                print('#' * self.__size)
