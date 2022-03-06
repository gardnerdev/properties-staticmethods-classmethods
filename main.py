class Driver:
    
    def __init__(self,name):
        self._name = name       # python convention -> private
    
    def name(self):             # getter function
        return self._name
    
    


if __name__ == "__main__":
    dd = Driver('Rick Falugia')
    print(dd.name())