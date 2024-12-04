
    
weight=int(input("enter the weight:"))
height=int(input("enter height in cm :"))
age=int(input("enter the age :"))
gender=input("enter gender :").lower()
print(age,weight,height,gender)

if gender=="male":

    BMR=10*weight+6.5*height -5*age +5

elif gender=="female":

    BMR=10*weight+6.5*height -5*age-161
else:

    print("*******please enter valid details********")

print(BMR)

activity_level=int(input("""
    select activity level                      
    press 1 for sedentary
    press 2 for lightly active                      
    press 3 for moderatively active
    press 4 for very active
    press 5 for extra active 
    """))
if activity_level==1:

    calorie=BMR*1.2

elif activity_level==2:
     
     calorie=BMR*1.375

elif activity_level==3:

    calorie=BMR*1.55

elif activity_level==4:
    calorie=BMR*1.4

elif activity_level==5:
    calorie=BMR*1.9
else:
    print("select valid  choice for activity level*********")

print(f"total number of calories you need in order to maintain your current weightis {calorie}")

target_weight=int(input("enter the weight to reduce in kg ;"))

duration=int(input("enter duration in weeks :"))

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print("daily calorie deficient is:",daily_calorie_deficit)

