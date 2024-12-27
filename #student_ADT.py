class Student:
    students = []

    def __init__(self, name, age, rollno, marks1, marks2):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2
        Student.students.append(self)

    def accept(self, name, age, rollno, marks1, marks2):
        # Check if student with the same rollno already exists
        for student in Student.students:
            if student.rollno == rollno:
                print(f'Student with roll number {rollno} already exists.')
                return
        student = Student(name, age, rollno, marks1, marks2)
        Student.students.append(student)

    def display(self):
        for student in Student.students:
            print('Name: ', student.name)
            print('Age: ', student.age)
            print('Rollno: ', student.rollno)
            print('Marks1: ', student.marks1)
            print('Marks2: ', student.marks2)
            print('-------------------------')

    def delete(self, rollno):
        for student in Student.students:
            if student.rollno == rollno:
                Student.students.remove(student)
                print('Student details deleted')
                break
        else:
            print('Student not found')

    def search(self, rollno):
        for student in Student.students:
            if student.rollno == rollno:
                print('Student found')
                print('Name: ', student.name)
                print('Age: ', student.age)
                print('Rollno: ', student.rollno)
                print('Marks1: ', student.marks1)
                print('Marks2: ', student.marks2)
                break
        else:
            print('Student not found')

    def update(self, rollno, name=None, age=None, marks1=None, marks2=None):
        for student in Student.students:
            if student.rollno == rollno:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if marks1:
                    student.marks1 = marks1
                if marks2:
                    student.marks2 = marks2
                print('Student details updated')
                break
        else:
            print('Student not found')

# creating object of class Student
std = Student('ExampleName', 20, 100, 85, 90)

# adding student details
std.accept('Rahul', 20, 101, 90, 80)
std.accept('Nishoodan', 21, 102, 80, 70)
std.accept('Aditya', 22, 103, 70, 60)
std.accept('Molay', 23, 104, 60, 50)

# displaying student details
std.display()

# updating student details
std.update(102, name='Nishoodan Updated', age=22, marks1=85, marks2=75)

# displaying student details after update
std.display()