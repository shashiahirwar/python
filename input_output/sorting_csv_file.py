from ast import Lambda


students = []

with open("/Users/shashi/Documents/Project/python3/input_output/names.csv") as file:
    for line in sorted(file):
        name, fruit, house = line.rstrip().split(",")
        student = {"name" : name, "fruit" : fruit, "house" : house}
        students.append(student)

#def get_fruit(student):
#    return student["fruit"]

for student in sorted(students, key=lambda student: student["fruit"]):
    print(f"{student['name']} likes {student['fruit']}")