
student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[35,33,38,],
    "anvin":[50,50,50]
}

student_avg_marks={k:sum(v)/len(v) for k,v in student_data.items()}
print(student_avg_marks)


# index=5

# for i,element in enumerate(student_data):

#     if i+1==index:

#         marks=student_data.get(element)

#         avg=sum(marks)/len(marks)
#         print(avg)

