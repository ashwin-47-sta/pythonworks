cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]


# print(f"total vehicles=>{len(cars)}")

# baleno_cars=[c.get("colors") for c in cars if c.get("name")=="baleno"]
# print(baleno_cars[0])

# all_brands={c.get("brand") for c in cars}
# print(all_brands)

amt_transmission=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(amt_transmission)

blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(blue_cars)

all_transmissions={t for c in cars for t in c.get("transmissions")}
print(all_transmissions)

colors={a for c in cars for a in c.get("colors")}
print(colors)


low_cost=min(cars,key=lambda d:d.get("price"))
print(low_cost.get("name"))

sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_name={c.get("name"):[c.get("price"),c.get("brand") ]for c in sorted_cars}

print(sorted_car_name)

