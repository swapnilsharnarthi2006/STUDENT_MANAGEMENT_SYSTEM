import json
def save_students(student_list):
    with open("data\student.json","w") as file:
        json.dump(student_list,file,indent=4)