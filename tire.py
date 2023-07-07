from abc import ABC
from car import Car


class Tire(Car, ABC):
    def needs_service(self):
        pass