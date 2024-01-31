class Car:
    def __init__(self,name,model,year) -> None:
        self.name=name
        self.model=model
        self.year=year
class Electric_Car(Car):
    def __init__(self, name, model, year,bat_capacity) -> None:
        super().__init__(name, model, year)
        self.bat_capacity=bat_capacity
    def display_info(self):
        print(f'Car Information:\n Year: {self.year} Name: {self.name} Model: {self.model} batttery Capacity: {self.bat_capacity}')
    
class Gas_Car(Car):
    def __init__(self, name, model, year,fuel_eff) -> None:
        super().__init__(name, model, year)
        self.fuel_eff=fuel_eff
    def display_info(self):
        print(f'Car Information:\n Year: {self.year} Name: {self.name} Model: {self.model} Fuel Efficiency: {self.fuel_eff} MPG')
    

car_type=input('Enter Car type(Electric/Gas): ').strip()
car_name=input('Enter Car Name: ')
car_model=input('Enter Car Model: ')
car_year=input('Enter Car Year: ')

if car_type.lower()=='electric':
    bat_capacity=input('Enter battery capacity(kWh): ')
    E_car=Electric_Car(car_name,car_model,car_year,bat_capacity)
    E_car.display_info()

elif car_type.lower()=='gas':
    fuel_eff=input('Enter Fuel Efficiency(MPG): ')
    Gas_car=Electric_Car(car_name,car_model,car_year,fuel_eff)
    Gas_car.display_info()
else:
    print("Invalid Car data")