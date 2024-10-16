class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):

        print('Hola, soy una persona')
    
class Student(Person):
    
    def __init__(self,name,age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f'Hola, mi id de estudiante es{self.student_id}')

student1=Student('Carlos','30','153045')

student1.greet()
