
employee={"eid":12,"name":"ram",
           "salary":25000,"department":"hr",
           "experience":6
          }

print(employee["salary"])


employee["contact"]=2345678
print(employee)

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)