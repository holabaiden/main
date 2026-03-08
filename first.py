class Student:
    amount_of_students = 0

    def __init__(self, height=160):
        self.height = height
        self.width = 151
        Student.amount_of_students += 1

jon = Student()
kim = Student(height=149)

print(f"I am {jon.height} kilometers tall and {jon.width} miles wide. And to remind you, yes, I'm taller than Kim, he's only {kim.height} kilometers tall")
print(f"Jon has {jon.amount_of_students} and Kim has {kim.amount_of_students}")