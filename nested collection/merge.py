
lst1=["apple","mango","onion","potato"]


lst2=[100,200]
result={}

for i in range(0,len(lst2)):

    list_one_element=lst1[i]
    list_two_element=lst2[i]
    result[list_one_element]=list_two_element

print(result)

balance_elements=lst1[len(lst2):]

for index,element in enumerate(balance_elements):
    result[element]=index+1

print(result)