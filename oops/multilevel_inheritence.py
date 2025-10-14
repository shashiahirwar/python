class Dog:
    def __init__(self, name):
        self.name =name

class labrador(Dog): #single inheritence
    def sound(self):
        print("labrador woo!!")

class GuideDog(labrador): #multilevel inheritence
    def guide(self):
        print(f"{self.name} Guides the way")

g=GuideDog("rocky")
print(g.guide())
g.sound()
