#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, name="aaa", breed="Pug"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if (type(name) != str or (len(name) not in range(1,26) )):
            print("Name must be string between 1 and 25 characters.")
        else: 
            self._name = name

    def get_breed(self):
        return self._breed
        
    def set_breed(self, breed):
        if (breed not in APPROVED_BREEDS):
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

            
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

        # if (type(name) != str or (len(name) not in range(1,26) )):
        #     print("Name must be string between 1 and 25 characters.")
        # else: 
        #     self.name = name


        #
        
    pass
