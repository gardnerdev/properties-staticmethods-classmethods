import random 

TRUCK_DRIVERS = [
    'Rick Falugia',
    'David Beck',
    'Danzel Want'
]


class Driver:
    
    _licenses = [
        'class D',
        'class E',
        'HR Heavy rigid',
        'MC'
    ]
    
    def __init__(self,name):
        self._name = name       # python convention -> private
    
    
    @property
    def name(self):             # getter function
        return self._name
    
    
    @name.setter                # @name refers to def name(self) function
    def name(self, name):
        
        if name not in TRUCK_DRIVERS:
            raise ValueError(f"{name} is not a truck driver")
        self._name = name
    
    
    @staticmethod           # not takes self a first argument (do not operate on object) - normal function which is attached to class
    def random_driver():    # static methods are used to implement factory functions -> generates instance of the class, objects
        return Driver(random.choice(TRUCK_DRIVERS))
        
    
    @classmethod
    def licences(cls):      # cls refers to class 
        return cls._licenses
    

if __name__ == "__main__":
    dd = Driver('Rick Falugia')
    # print(dd.name())
    
    # after added property decorator
    print(dd.name)
    
    # after added setter and validation
    # dd.name = "Ricky Martin"
    # print(dd.name)
    
    random_driver = Driver.random_driver()
    print(f"Randomly generated driver: {random_driver.name}")
    
    print(Driver.licences())

    dw = Driver('Danzel Want')
    dw._licenses = ['MC']
    print(dw.licences()) # returns the same value because it refers to class, not object
    
    dw.__class__._licenses = ['MC']
    print(dw.licences()) # changes the list in the driver class, not the property for dw object!
    
    
    print(Driver.licences())