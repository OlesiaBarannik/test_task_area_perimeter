import area_perimeter
import unittest

class AreaPerimeterTest(unittest.TestCase):

    def test_Rectangle(self):
        self.assertEqual(area_perimeter.Rectangle("Rectangle TopRight 4 3 BottomLeft 2 1").get_Result(), "Rectangle Perimeter 8.0 Area 4.0")
        self.assertEqual(area_perimeter.Rectangle("Rectangle TopRight 6 3 BottomLeft 2 1").get_Result(), "Rectangle Perimeter 12.0 Area 8.0")

    def test_Square(self):
        self.assertEqual(area_perimeter.Square("Square TopRight 1 1 Side 1").get_Result(), "Square Perimeter 4.0 Area 1.0")
        self.assertEqual(area_perimeter.Square("Square TopRight 4 3 Side 5").get_Result(), "Square Perimeter 20.0 Area 25.0")

    def test_Circle(self):
        self.assertEqual(area_perimeter.Circle("Circle Center 1 1 Radius 2").get_Result(), "Circle's circumference 12.57 Area 12.57")
        self.assertEqual(area_perimeter.Circle("Circle Center 2 3 Radius 4").get_Result(), "Circle's circumference 25.13 Area 50.27")

if __name__ == '__main__':
    unittest.main()

