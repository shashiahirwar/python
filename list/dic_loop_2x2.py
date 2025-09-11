students ={"Harry" : "Gryffindor",
           "Draco" : "Slytherin",
           "Luna" : "Ravenclaw",
           "Cedric" : "Hufflepuff"
           }#dictionary with key value pairs
for student in students: #for loop to iterate over dictionary
    print(student, students[student], sep=", ")#printing keys of dictionary
