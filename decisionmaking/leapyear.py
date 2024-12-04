year=int(input("enter the year:"))

# t is evenly divisible by 4 
# If it is also evenly divisible by 100, it must also be evenly divisible by 400

if (year%100 !=0 and year%4==0) or (year%100==0 and year%400==0):
    print("leap year")

else:

    print("not a leap year")