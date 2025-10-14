class Calculator:
    def add(self, *args):
        return sum(args)
    
calc=Calculator()
print(calc.add(10,10))
print(calc.add(10,10,10))
print(calc.add(10,10,10,10))