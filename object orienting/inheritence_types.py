
class Grandparent:

    def m1(self):

        print("grand parent class m1 method")

class parent():

    def m2(self):

        print("parent class m2 method")

class child(parent,Grandparent):

    def m3(self):

        print("child class  m3 method ")

child_instance=child()

child_instance.m3()
child_instance.m2()
child_instance.m1()