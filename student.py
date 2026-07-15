class Student:
    def __init__(self, student_id, name, age, branch, year, email, phone_number):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.branch = branch
        self.year = year
        self.email = email
        self.phone_number = phone_number

    def display(self):
        print(f"student ID: {self.student_id}")
        print(f"name :{self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {self.branch}")
        print(f"Year: {self.year}")
        print(f"Email: {self.email}")
        print(f"Phone Number : {self.phone_number}")

    def to_dict(self):
        return{
            "student_id" : self.student_id,
            "name" : self.name,
            "age" : self.age,
            "branch" : self.branch,
            "year" : self.year,
            "email" : self.email,
            "phone_number" : self.phone_number
        }