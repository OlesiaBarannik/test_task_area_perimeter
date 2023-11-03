from math import pi
class Shape:
    def __init__(self, str_input):
        self.list_input = str_input.split(" ")

    def set_data_for_calculation(self):
        return None

    def get_Perimeter(self):
        return None

    def get_Area(self):
        return None

    def get_Result(self):
        return None


class Rectangle(Shape):
    def __init__(self, str_input):
        super().__init__(str_input)
        self.set_data_for_calculation()
    def set_data_for_calculation(self):
        self.a = float(self.list_input[2]) - float(self.list_input[-2])
        self.b = float(self.list_input[3]) - float(self.list_input[-1])

    def get_Perimeter(self):
        return self.a*2 + self.b*2

    def get_Area(self):
        return self.a * self.b

    def check_side(self):
        if self.a <= 0 or self.b <= 0:
            return False
        return True

    def get_Result(self):
        if self.check_side() is True:
            return (f"{self.list_input[0]} Perimeter {self.get_Perimeter()} Area {self.get_Area()}")
        return "Not valid data"


class Square(Shape):
    def __init__(self, str_input):
        super().__init__(str_input)
        self.set_data_for_calculation()
    def set_data_for_calculation(self):
        self.a = float(self.list_input[-1])
        self.b = float(self.list_input[-1])

    def get_Perimeter(self):
        return self.a * 2 + self.b * 2

    def get_Area(self):
        return self.a * self.b

    def check_side(self):
        if self.a < 0:
            return False
        return True

    def get_Result(self):
        if self.check_side() is True:
            return (f"{self.list_input[0]} Perimeter {self.get_Perimeter()} Area {self.get_Area()}")
        return "Not valid data"

class Circle(Shape):
    def __init__(self, str_input):
        super().__init__(str_input)
        self.set_data_for_calculation()

    def set_data_for_calculation(self):
        self.radius = float(self.list_input[-1])


    def get_Perimeter(self):
        return round(2 * self.radius * pi, 2)

    def get_Area(self):
        return round(pi * self.radius**2, 2)

    def check_side(self):
        if self.radius < 0:
            return False
        return True

    def get_Result(self):
        if self.check_side() is True:
            return (f"{self.list_input[0]}'s circumference {self.get_Perimeter()} Area {self.get_Area()}")
        return "Not valid data"



