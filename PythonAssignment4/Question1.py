# parent
class Triangle:
    def __init__(self):
        # Read the three sides from the user
        self.a = float(input("Enter the length of side a: "))
        self.b = float(input("Enter the length of side b: "))
        self.c = float(input("Enter the length of side c: "))


# Subclass
class TriangleArea(Triangle):
    def __init__(self):
        super().__init__()  # Initialize the parent class

    def calculate_area(self):
        # Calculate the semi-perimeter
        s = (self.a + self.b + self.c) / 2
        TriangleArea = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return TriangleArea


triangle_area = TriangleArea()
area = triangle_area.calculate_area()
print(f"The area of the triangle is: {area}")
