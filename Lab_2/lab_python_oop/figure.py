from abc import ABC, abstractmethod

#Абстрактный класс «Геометрическая фигура»
class Figure(ABC):
    @abstractmethod
    def square(self):
        pass
