

class student:

    rollnumber:int

    name:str

    age:int

    course:str

    def set_student(self,name,rollnumber,age,course):


        self.name=name

        self.rollnumber=rollnumber

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.rollnumber,self.age,self.course)

student_instance1=student()



student_instance1.set_student("ashwin",100,21,"django")

student_instance1.display()