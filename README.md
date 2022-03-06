# properties-staticmethods-classmethods
Python training project



# Run
`python3 main.py`




# Description

`@property` changes the behaviour of the function in such a way, that we need to 
call the function, we can refer to it


`@staticmethod`: does not take self as a first argument (does not operate on object)
    normal function which is attached to class \
    e.g:
    `def random_driver()` : static methods are used to implement factory functions -> generates instance of the class, objects

    
`@classmethod` \
    `def licences(cls)` : cls refers to class