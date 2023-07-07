from serviceable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass
