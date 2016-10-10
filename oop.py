class Car(object):
    def __init__(self, name):
        self.__updateSoftware()   
        self.name = name
 
    def __updateSoftware(self):
        print 'Updating software...'

    def fuel(self):
        print 'Fueling Car...'

    def drive(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 

#Demonstrating Inheritance
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar breaking!'

#Demonstrating Inheritance
class Truck(Car):
    def drive(self):
        return 'Truck is driving slowly because it is heavily loaded.'
 
    def stop(self):
        return 'Truck breaking!'
 

bugatti = Car('Veyron')
bugatti.fuel()
#bugatti.__updateSoftware()  not accesible from object.
try:
    bugatti.__updateSoftware()
except:
    print("This demonstrates Encapsulation. __updateSoftware() is not accesible from object")

cars = [Truck('Oil-Truck'), Truck('Milk-Truck'), Sportscar('Z3')]

# Demonstrating Polymorphism
for car in cars:
    print car.name + ': ' + car.drive()