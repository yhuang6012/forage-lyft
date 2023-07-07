from tire import Tire


class OctoprimeTires(Tire):
    def __init__(self, sensors):
        self.sensors = sensors
        
    def needs_service(self):
        sum = 0
        for e in self.sensors:
            sum += e
        if sum >= 3:
            return True
        else:
            return False