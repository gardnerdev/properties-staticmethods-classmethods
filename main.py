class Driver:
    
    def __init__(self,name):
        self._name = name       # python convention -> private
    
    
    @property
    def name(self):             # getter function
        return self._name
    
    
    @name.setter                # @name refers to def name(self) function
    def name(self, name):
        self._name = name
    

if __name__ == "__main__":
    dd = Driver('Rick Falugia')
    # print(dd.name())
    
    # after added property decorator
    print(dd.name)
    
    # after added setter
    dd.name = "Ricky Martin"
    print(dd.name)