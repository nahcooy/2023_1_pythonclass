from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return 0.5 * self.w * self.h

    def perimeter(self):
        return self.w + self.h + ((self.w ** 2 + self.h ** 2) ** 0.5)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14 * self.r


class RegularHexagon(Shape):
    def __init__(self, l):
        self.l = l

    def area(self):
        return (3 * (3 ** 0.5) * self.l ** 2) / 2

    def perimeter(self):
        return 6 * self.l


def main():
    shapes = [
        Rectangle(5, 2),
        Rectangle(8, 5),
        Triangle(4, 5),
        Triangle(4, 7),
        Rectangle(4, 5),
        Triangle(3, 4),
        Circle(2),
        RegularHexagon(5)
    ]

    for shape in shapes:
        if isinstance(shape, Rectangle):
            print("도형: 직사각형")
        elif isinstance(shape, Triangle):
            print("도형: 삼각형")
        elif isinstance(shape, Circle):
            print("도형: 원")
        elif isinstance(shape, RegularHexagon):
            print("도형: 정육각형")

        print(f"넓이는: {shape.area():.2f}")
        print(f"둘레는: {shape.perimeter():.2f}")
        print()


if __name__ == "__main__":
    main()
