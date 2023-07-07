from car import Car
from abc import ABC

class Battery(Car, ABC):
    def needs_service(self):
        pass