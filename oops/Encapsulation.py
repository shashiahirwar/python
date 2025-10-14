class Dog:
    def __init__(self, name, breed, age):
        self.name=name # public attribute
        self._breed=breed #protected attribue
        self.__age=age #private attribue
    #public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"
    #Getter and setter
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age=age
        else:
            print("Invalid age")
dog =Dog("momo", "frenchBulldog", 3)
print(dog.name) #public access
print(dog._breed)
print(dog.get_info())
dog.set_age(3)
print(dog.get_info)
    
        