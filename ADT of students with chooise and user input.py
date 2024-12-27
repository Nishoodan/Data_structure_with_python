# Program for student ADT with chooise and user input

class Student:
    student = []
    
    def __init__(self, name, rollno, subject, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.subject = subject
        self.marks1 = marks1
        self.marks2 = marks2
    
    @staticmethod
    def add(student):
        print('Enter student details')
        name = input("Enter name: ")
        rollno = int(input("Enter rollno: "))
        subject = input("Enter subject: ")
        marks1 = int(input("Enter marks1: "))
        marks2 = int(input("Enter marks2: "))
        Student.student.append(Student(name, rollno, subject, marks1, marks2))
        
    @staticmethod
    def display(students):
        if not students:
            print('No student details')
        else:
            print('Total Student details')
            for student in students:
                print('Name:', student.name)
                print('Rollno:', student.rollno)
                print('Subject:', student.subject)
                print('Marks1:', student.marks1)
                print('Marks2:', student.marks2)
                
            

    @staticmethod
    def search(student, rollno):
        for index,students in enumerate(student):
            if students.rollno == rollno:
                print(students.name)
                print(students.rollno)
                print(students.subject)
                print(students.marks1)
                print(students.marks2)
                return index
        else:
            print('Student not found')
            return -1
    
    @staticmethod
    def update(student, rollno):
        up = Student.search(student, rollno)
        if up != -1:
            nrollno = input('Enter new rollno: ')
            student[up].rollno = nrollno
            print('Rollno updated')
    
    @staticmethod
    def delete(student, rollno):
        a = Student.search(student, rollno)
        if a != -1:
            del student[a]
            print('Student details deleted')
        
    def menu():
        while True:
            print('\n Operations menu \n')
            print('1. Add student details')
            print('2. Display student details')
            print('3. Search for student')
            print('4. Update student details')
            print('5. Delete student details')
            print('6. Exit')

            choice = int(input('Enter your choice from 1-5: '))
            if choice == 1:
                Student.add(Student.student)
                
            elif choice == 2:
                Student.display(Student.student)
                
            elif choice ==3:
                rollno = int(input('Enter rollno to search:'))
                Student.search(Student.student, rollno)
            
            elif choice ==4:
                rollno = int(input('Enter rollno to update: '))
                nrollno = int(input('Enter new roll no: '))
                Student.update(Student.student,rollno)
                
            elif choice ==5:
                rollno = int(input('Enter rollno to delete:'))
                Student.delete(Student.student ,rollno)
            
            else:
                if choice == 6:
                    break

Student.menu()
                
                