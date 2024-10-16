# Complejidad de la programacion orientada a objetos. 4 Pilares.
# Herencia,Encapsulación,Abstracción,Polimorfismo.

class Vehicle:

    def __init__(self,brand,model,price):
        #Encapsulación
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehículo{self.brand} ha sido vendido')
        else:
            print(f'El vehículo{self.brand} no esta disponible')
#Abstracción. Uso de métodos. Por ejemplo, método get. 
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')

    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')


class Car(Vehicle):

#Polimorfismo. El código se puede repetir infinitas veces, y puede tener un comportamiento diferente.

    def start_engine(self):
        if not self.is_available:
            return f'El motor del coche{self.brand} no esta en marcha'
        else:
            return f'El coche{self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del coche{self.brand} se ha detenido'
        else:
            return f'El coche{self.brand} esta en marcha'
        

#Polimorfismo

class Bike(Vehicle):

    def start_engine(self):
        if not self.is_available:
            return f'La bicicleta{self.brand} no esta en marcha'
        else:
            return f'La bicicleta{self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'La bicicleta{self.brand} se ha detenido'
        else:
            return f'La bicicleta{self.brand} esta en marcha'
        
#Polimorfismo

class Truck(Vehicle):

    def start_engine(self):
        if not self.is_available:
            return f'El motor del camión{self.brand} no esta en marcha'
        else:
            return f'El camión{self.brand} no esta disponible'
        
    def stop_engine(self):
        if self.is_available:
            return f'El motor del camión{self.brand} se ha detenido'
        else:
            return f'El camión{self.brand} esta en marcha'
        
class Customer:
    
    def __init__(self,name):
        self.name = name
        self.purchased_vehicle = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicle.append(vehicle)
        else:
            print(f'Lo siento{vehicle.brand}no esta disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = 'Disponible'
        else:
            availability = 'No disponible'
            print(f'El{vehicle.brand}esta{availability} y cuesta{vehicle.get_price()}')

class Dealership:

    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f'El{vehicle.brand} ha sido añadido al inventario')

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f'El cliente{customer.name} ha sido añadido al sistema')

    def show_available_vehicle(self):
        print('vehículo disponible en la tienda')
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f'{vehicle.brand} por {vehicle.get_price()}')

car1 = Car('Fiat','Palio','20000')
bike1 = Bike('Venzo','mountain bike','5000')
Truck1 = Truck('Volvo','RZ-31','50000')

customer1 = Customer('Carlos')

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(Truck1)
dealership.show_available_vehicle()
dealership.register_customers(customer1)
customer1.inquire_vehicle(car1)
customer1.buy_vehicle(car1)
dealership.show_available_vehicle()

