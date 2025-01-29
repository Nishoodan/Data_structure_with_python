# Program for student ADT with chooise and user input

class Student:
    students_list = []

    def __init__(self, name, rollno, subject):
        self.name, self.rollno, self.subject = name, rollno, subject

    def __str__(self):
        return f"Name: {self.name}, Rollno: {self.rollno}, Subject: {self.subject}"

    @staticmethod
    def add():
        Student.students_list.append(Student(input("Name: "), int(input("Rollno: ")), input("Subject: ")))

    @staticmethod
    def display():
        print("\n".join(map(str, Student.students_list)) if Student.students_list else "No students available.")

    @staticmethod
    def search(rollno):
        for i, s in enumerate(Student.students_list):
            if s.rollno == rollno:
                print(s)
                return i
        print("Student not found.")
        return -1

    @staticmethod
    def update(rollno):
        idx = Student.search(rollno)
        if idx != -1:
            Student.students_list[idx].rollno = int(input("Enter new Roll No: "))
            print("Updated successfully.")

    @staticmethod
    def delete(rollno):
        idx = Student.search(rollno)
        if idx != -1:
            del Student.students_list[idx]
            print("Deleted successfully.")

    @staticmethod
    def menu():
        options = {
            1: Student.add,
            2: Student.display,
            3: lambda: Student.search(int(input("Rollno: "))),
            4: lambda: Student.update(int(input("Rollno: "))),
            5: lambda: Student.delete(int(input("Rollno: ")))
        }

        while (choice := int(input("\n1. Add\n2. Display\n3. Search\n4. Update\n5. Delete\n6. Exit\nChoose: "))) != 6:
            options.get(choice, lambda: print("Invalid choice."))()


Student.menu()

                
