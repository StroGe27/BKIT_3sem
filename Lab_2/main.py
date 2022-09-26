from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import sys
def get_side_rad(prompt = "Введите значение стороны"):
    print(prompt)
    try:
        # Пробуем прочитать значение из командной строки
        side_str = sys.argvp
    except:
        # Вводим с клавиатуры
        side_str = input()
    # Обрабатываем неправильный ввод
    while True:
        try:
            side = float(side_str)
        except:
            print("Введены неправильные данные.")
            side_str = input()
        else:
            return side
def get_color(termpt):
    print("Введите цвет будущего", termpt)
    return str(input())
def main():
    print("Выберете тип ввода:\n1 - с клавиатуры в консоли\n2 - вариант 16")
    choise = int(input())
    cowsay.cow('Hello World')
    if choise == 1:
        r  = Rectangle(get_color("прямоугольника"), get_side_rad(), get_side_rad())
        c = Circle(get_color("круга"), get_side_rad("Введите радиус"))
        s = Square(get_color("квадрата"), get_side_rad())
        print(r, c, s, sep = "\n")
    else:
        print(Rectangle("синего", 16, 16))
        print(Circle("зеленого", 16))
        print(Square("красного", 16))

if __name__ == "__main__":
    main()
