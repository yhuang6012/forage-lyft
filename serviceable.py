from abc import ABC

class Servicable(ABC):
    def needs_service(self):
        pass