#!/usr/bin/python3
"""Square Class"""
class Square:
    """square class"""
    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """ Calculates area of the square"""
        return self.__size * self.__size
    
    def my_print(self):
        """Prints square of # in size of square size"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
