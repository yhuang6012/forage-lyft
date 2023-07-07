from car import Car
from capulet_engine import CapuletEngine
from spindler_battery import SpindlerBattery
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from nubbin_battery import NubbinBattery


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        if (CapuletEngine.needs_service(current_mileage, last_service_mileage) == True 
            or SpindlerBattery.needs_service(last_service_date, current_date) == True):
            Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))
    
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        if (WilloughbyEngine.needs_service(current_mileage, last_service_mileage) == True 
            or SpindlerBattery.needs_service(last_service_date, current_date) == True):
            Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))
    
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        if SternmanEngine.needs_service(warning_light_on) == True or NubbinBattery.needs_service(last_service_date, current_date) == True:
            Car(SternmanEngine(warning_light_on), NubbinBattery(last_service_date, current_date))
    
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        if WilloughbyEngine.needs_service(current_mileage, last_service_mileage) == True or NubbinBattery.needs_service(last_service_date, current_date) == True:
            Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))
        
        
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        if CapuletEngine.needs_service(current_mileage, last_service_mileage) == True or  NubbinBattery.needs_service(last_service_date, current_date) == True:
            Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))