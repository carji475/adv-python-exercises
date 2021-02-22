#a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (___init___) and define a method that returns the full name of the person as a combined string.
class Person(object):
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname
    
    @property 
    def name(self):
        return self._firstname + ' ' + self._lastname
        


#b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super(Student,self).__init__(firstname, lastname)
        self._subject = subject
    
    def printNameSubject(self):
        print(self.name+', '+self._subject)



#c. You should be able now to use your "Student" class like this:
#In [1]: from classroom import Student
#In [2]: me = Student('Benedikt', 'Daurer', 'physics') 
#In [3]: me.printNameSubject() 
#Benedikt Daurer, physics


#d. Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches.
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super(Teacher,self).__init__(firstname, lastname)
        self._course = course
    
    def printNameSubject(self):
        print(self.name+', '+self._course)



















