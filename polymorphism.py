from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.base + self.height

class pizza(circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [circle(5), rectangle(4, 5), square(5), triangle(4, 5), pizza("pepperoni", 5)]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")
    print(f"Perimeter of {shape.__class__.__name__}: {shape.perimeter()}")
    if isinstance(shape, pizza):
        print(f"Topping of {shape.__class__.__name__}: {shape.topping}")   

    
