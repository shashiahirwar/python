class Dog:
    def __init__(self, name):
        self.name = name
        
class Friendly:
    def greet(self):
        print("Friendly message")

class WhichDogisFrnd(Dog,Friendly):# Multiple Inheritance
    def greet(self):
        print("thats the dog")
        
thisDog= WhichDogisFrnd("Momo")
print(thisDog.name)
thisDog.greet()
thisDog.findout()
