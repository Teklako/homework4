#დავალება1
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}.school@edu.ge")
class Leacture(People):
    def __init__(self,firstname, lastname,salary):
        super().__init__(firstname,lastname)
        self.salary = salary
    def get_email(self):
        print(f"{self.firstname}.{self.lastname}@edu.ge, ლექტორის ხელფასია: {self.salary}")

class Student(People):
    def __init__(self,firstname, lastname,courses):
        super().__init__(firstname,lastname)
        self.courses = list(courses)
    def get_email(self):
        print(f"{self.firstname}.{self.lastname}1@edu.ge,სტუდენტის საგნებია:,{self.courses}")
f1 = People("Tekla", "kvaratskhelia")
f1.get_email()
f2 = Leacture("tekla", "kvaratskhelia",80)
f2.get_email()
f3 = Student("tekla", "kvaratskhelia",['Biologia','Georgia','Python','English'])
f3.get_email()

#დავალება2
class libraryitem:
    def __init__(self, title, subject,status):
        self.title = title
        self.subject = subject
        self.status = status
    def __str__(self):
        if self.status == "occupied":
            return ("dajavshnilia")
        if self.status == "available":
            return ("xelmisawvdomia")
    def booking(self):
        if self.status == "available":
            print(f"{self.status}")
class Book(libraryitem):
    pass
    def __init__(self,title,subject, status, ISBN, authors ):
        super().__init__(title,subject, status)
        self.ISBN = ISBN
        self.authors = authors
    def booking(self):
        if self.status == "available":
            print(f"{self.status}")
class Magazine(libraryitem):
    pass
    def __init__(self,status,journalName, volume,title=None,subject=None):
        super().__init__(status,title,subject)
        self.journalName = journalName
        self.volume = volume
    def __str__(self):
        if self.status == "occupied":
            return ("dajavshnilia")
        if self.status == "available":
            return ("xelmisawvdomia")

    def booking(self):
        if self.status == "occuped":
            print(f"{self.status}")
class CD(libraryitem):
    pass
    def __init__(self,title, status,subject=None):
        super().__init__(title,status,subject)
    def __str__(self):
        if self.status == "occupied":
            return ("dajavshnilia")
        if self.status == "available":
            return ("xelmisawvdomia")
    def booking(self):
        if self.status == "occuped":
            print(f"{self.status}")
obj1 = libraryitem("bios","biologia","occuped")
print(obj1.title,obj1.subject,obj1.booking())




#დავალება3
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname} aris {self.age} wlis."

class Employee:
    def __init__(self, profession, monthly_salary, working_hours):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

class Doctor(Person, Employee):
    def __init__(self, firstname, lastname, age, profession, monthly_salary, working_hours):
        Person.__init__(self, firstname, lastname, age)
        Employee.__init__(self, profession, monthly_salary, working_hours)

    def hourly_salary(self):
        hourly_rate = self.monthly_salary / (self.working_hours * 4)
        return hourly_rate

    def perform_operation(self):
        return f" i'm {doctor.firstname} {doctor.lastname} ,{doctor.age} wlis. i'm a {doctor.profession}"


firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
age = int(input("Enter age: "))


profession = input("Enter profession: ")
monthly_salary = int(input("Enter monthly salary: "))
working_hours = int(input("Enter working hours: "))

doctor = Doctor(firstname, lastname, age, profession, monthly_salary, working_hours)

print(doctor.perform_operation())
print(f"my Monthly salary is- {doctor.monthly_salary}")
print(f"my Working hours is - {doctor.working_hours}")
hourly_rate = doctor.hourly_salary()
print(f"my Hourly salary is- {hourly_rate}\n")











