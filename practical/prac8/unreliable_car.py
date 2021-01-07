"""
CP1404 Practical
UnreliableCar class
"""
from car import Car
from random import randint


class UnreliableCar(Car):
    """Class for any car that only drive when the random number is less than car's reliability """

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Only drive when the random number is less than car's reliability"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        return super().drive(distance)
