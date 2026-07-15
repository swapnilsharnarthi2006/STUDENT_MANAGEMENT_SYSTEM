from student import Student
from database import save_students
student1 = Student(
    "101",
    "swapnil",
    "20",
    "cseds",
    "2025",
    "swapnil@gmail.com",
    "8263983380"
   
)
data = [student1.to_dict()]
save_students(data)
print("done!!!!")