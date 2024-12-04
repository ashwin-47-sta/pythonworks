

employee={"id":12,"name":"ram",
          "salary":25000,"department":"hr",
          "age":23}

print(employee.get("department"))

employee.pop("salary")
print(employee)

# for k in employee.keys():


#     print(k)


for v in employee.values():#fetch all values=values()


    print(v)


# get(key),pop(key),keys(),values(),
# fetch key and values items()


for k,v in employee.items():

    print(k,v)

    