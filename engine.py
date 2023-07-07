from car import Car
from abc import ABC

class Engine(Car, ABC):
    def needs_service(self):
        pass