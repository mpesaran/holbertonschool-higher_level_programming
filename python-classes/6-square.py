#!/usr/bin/python3
"""Square Class"""
class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if (
            not isinstance(position, tuple)
            or len(position) != 2      
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        for num in range(2): 
            if not isinstance(position[num], int) or position[num] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
    
    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        """ Calculates area of the square"""
        return self.__size * self.__size
    
    def my_print(self):
        """Prints square of # in size of square size and position(x,y)"""
        if self.__size == 0:
            print("")
        else:
            for m in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print("_", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
