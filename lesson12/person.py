from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # Encapsulation using @property
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("Weight must be positive!")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive!")

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print("\n===== PERSON INFORMATION =====")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Weight : {self.weight} kg")
        print(f"Height : {self.height} m")
        print(f"BMI    : {self.calculate_bmi():.2f}")
        print(f"Category: {self.get_bmi_category()}")