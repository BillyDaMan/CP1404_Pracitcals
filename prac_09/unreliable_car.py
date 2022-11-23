from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drives the car and bases the car's reliability on a random number"""
        random_number = randint(1, 100)
        if self.reliability <= random_number:
            distance = 0
        distance = super().drive(distance)
        return distance
