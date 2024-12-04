


def add_numbers(*args):


    print(args)

add_numbers(10,20)
add_numbers(10,20,30)  


def second_max_number(*args):

    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]

print(second_max_number(10,11,12,13))
print(second_max_number(10,11,12,13,14,15))