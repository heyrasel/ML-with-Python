class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}")
    

car = Car("Mercedes", "Mercedes-Benz E-Class", 2025)
car.display_info()

