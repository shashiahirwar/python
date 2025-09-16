import csv
students = []

with open("/Users/shashi/Documents/Project/python3/input_output/names.csv") as file:
    reader=csv.reader(file)
    for name in reader:
        students.appeand ({"name" : name, "home" : home})
        
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['name']}")
    