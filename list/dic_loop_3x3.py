students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
    {"name": "Cedric", "house": "Hufflepuff", "patronus": "Badger"}
]

for student in students: #for loop to iterate over list of dictionaries
    print(student["name"], student["house"], student["patronus"], sep=", ")#printing values of dictionary keys
    students.reverse() #reversing the list of dictionaries