from tire import Tire


class CarriganTires(Tire):
    def __init__(self, sensors):
        self.sensors = sensors
        
    def needs_service(self):
        for e in self.sensors:
            if e >= 0.9:
                return True
        return False