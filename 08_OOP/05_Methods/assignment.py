class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height

    def get_height(self) -> float:
        return self.__height

     base = Rectangle.get_base()

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
      area = Rectangle.get_area()
    def __str__(self) -> str:
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)
    
