class Avtomobile:


    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

Tayota = Avtomobile("Tayota","Landcruiser","Green")

print(f'Brand of car:{Tayota.brand} model:P{Tayota.model} color:{Tayota.color}')


class Employee:
    def __init__(self, name, surname, gender, date_birth):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.gender}, {self.date_birth}'

empl = Employee("beks", "tur", "male", "27 april")
print(empl)

class Human:
    def __init__(self, name, age, favorite_lesson):
        self.name = name
        self.age = age
        self.favorite_lesson = favorite_lesson

    def __str__(self):
         return f'{self.name}, {self.age}, {self.favorite_lesson}'

class Teacher(Human):
    def __init__(self, speciality, salary):
        self.speciality = speciality
        self.salary = salary

    def __str__(self):
         return f'{self.speciality}, {self.salary}'

class Student(Human):
    def __init__(self, grade):
        self.grade = grade

    def __str__(self):
         return f'{self.grade}'



Adilet = Human("Adilet", 18, "MATH")
Beks = Teacher("Programmer", 50000)
Vadim = Student(3)
    
print(Adilet, Beks, Vadim, sep = "\n")



