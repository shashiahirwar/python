class Dog:
    #class attribute
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1=Dog("Momo", 2)
print(dog1.name)
print(dog1.age)