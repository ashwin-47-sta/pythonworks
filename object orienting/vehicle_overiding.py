


class parent:

    def vehicle(self):

        self.bikes=["passion plus ","activa"]

        return self.bikes
    


class child(parent):

    def vehicles(self):

        self.bikes=super().vehicle()
        self.bikes.append("hunter")

        return self.bikes


child_instance1=child()




