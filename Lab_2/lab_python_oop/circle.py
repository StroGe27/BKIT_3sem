from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    type = "Круг"

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def square(self):
        return math.pi*(self.r**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(Circle.type, self.fc.colorproperty, self.r, self.square())
