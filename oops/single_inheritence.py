class Dog:
    def __init__(self, name):
        self.name = name

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")
        
lab =Labrador("jackey")
print(lab.name)
lab.sound()
#single inheritence