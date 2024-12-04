

class Bank:

    def __init__(self,acno,balance,ac_type,customer_name):

        self.acno=acno

        self.balance=balance

        self.ac_type=ac_type

        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account {self.acno} has been credited with amount {amount} avl bal {self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            self.balance-=amount

            print(f"your account {self.acno} has been debited with amount {amount} with avl bal {self.balance}")

        else:

            print("insuffficient balance")

    def get_balance(self):
        
        print("your aval bal",self.balance)


customer_instance=Bank(1000,2500,"saving","aseed")

customer_instance.deposit(1000)