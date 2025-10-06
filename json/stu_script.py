# Reading Data from json file 
import json
with open("stu_data.json", 'r' ) as file:
    data=json.load(file)
# print(data)
#working status -- true

#finding a student 
student_id = 1
found = False

for student in data:
    if student["student_id"] == student_id:
        print(f"Student found with ID {student_id} --> {student['name']['first']} {student['name']['last']}")
        found = True
        break

if not found:
    print(f"Student with ID {student_id} not found")


