
# def display_mobile_data(**Kwargs):

#     print(Kwargs.get("name"))
#     print(Kwargs.get("price"))

# display_mobile_data(name="oneplus",price=32000,display="amoled")



def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)

    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result=result*num

        return result

print(calculator(10,20,30,operation="*"))


def student_iinfo(*args,**kwargs):

    if kwargs.get("operation")=="total":

        return sum(args)

    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)

print(student_iinfo(45,43,44,operation="avg"))


def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="False":

        return sorted(args)

print(sort_numbers(1,2,6,4,15,11,reverse="True"))



