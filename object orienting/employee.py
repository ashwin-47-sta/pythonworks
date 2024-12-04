class person:
    def _init_(self, name, age):
        self.name=name
        self.age=age
    
    def display_person_info(self):
        print(f"name=>{self.name}, age=>{self.age}")
    
class employee:
    def _init_(self, emp_id, salary):
        self.emp_id=emp_id
        self.salary=salary
    
    def display_employee_info(self):
        print(f"{self.emp_id}=>{self.salary}")
    
class Manager(person,employee):
    def _init_(self, name, age, emp_id, salary, department):
        person._init_(self,name, age)
        employee._init_(self,emp_id, salary)
        self.department=department

    def display_manager_info(self):
        self.display_person_info()
        self.display_employee_info()
        print (self.department)

manager_instance1=Manager(32,"hari","e01",54000,"hr")
manager_instance1.display_manager_info()
    

# manager_instance1=Manager("Rob",29,991,79000,"HR")
# manager_instance1.display_person_info()
# manager_instance1.display_employee_info()