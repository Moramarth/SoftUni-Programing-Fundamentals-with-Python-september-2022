class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        result = self.diameter * Circle.__pi
        return result

    def calculate_area(self):
        result = ((self.diameter / 2)**2) * Circle.__pi
        return result

    def calculate_area_of_sector(self, angle):
        result = (angle/360) * (((self.diameter / 2) ** 2) * Circle.__pi)
        return result


