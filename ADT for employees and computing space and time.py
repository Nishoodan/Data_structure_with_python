import time
import tracemalloc

class Employee:
    def __init__(self):
        self.name = input('Enter the name: ')
        self.desig = input('Enter the designation: ')
        self.salary = int(input('Enter the salary: '))

    def display(self):
        print(f"Name: {self.name}, Designation: {self.desig}, Salary: {self.salary}")


# Main program
start_time = time.process_time()
tracemalloc.start()

employees = []
while input("Add an employee? (y/n): ").lower() != 'n':
    employees.append(Employee())

print("\nEmployee Details:")
for emp in employees:
    emp.display()

# Performance metrics
end_time = time.process_time()
current, peak = tracemalloc.get_traced_memory()
print(f"\nMemory Used (Current: {current}, Peak: {peak}) bytes")
print(f"Time Taken: {end_time - start_time:.2f} seconds")
tracemalloc.stop()
