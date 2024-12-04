


class shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)


class expreeshipping(shipping):


    def calculate_shipping_cost(self,weight):


        print(weight*20)

class standardshipping(shipping):
    pass
    
    def calculate_shipping_cost(self, weight):
        print(weight*10)


expo_instance=expreeshipping()

expo_instance.calculate_shipping_cost(10)

std_instance=standardshipping()

std_instance.calculate_shipping_cost(10)