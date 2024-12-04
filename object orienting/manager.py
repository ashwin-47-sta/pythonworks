class Person:

    def _init_(self,name,age):

        self.name=name
        self.age=age

    def dispaly_person_info(self):

        print(self.name,self.age)

class Employee:

    def _init_(self,eid,salary):

        self.eid=eid
        self.sarary=salary

    def dispaly_employee_info(self):

        print(self.eid,self.sarary)

class Manager(Person,Employee):

    def _init_(self,name,age,eid,salary,department):

        Person._init_(self,name,age)
        Employee._init_(self,eid,salary)
        self.department=department

    def dispaly_manager_info(self):

        self.dispaly_person_info()

        self.dispaly_employee_info()

        print(self.department)

manager_instance1=Manager("vaishnav", 29, "e2019", 100000, "Developer" )
manager_instance1.dispaly_manager_info()