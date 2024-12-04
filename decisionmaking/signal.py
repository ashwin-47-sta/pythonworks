

#syntax
#if condition:
   #stmt1

#elif condition2:
   #stmt2

#elif condition3:
    #stmt3

# else:
  #default stmt

signal=input("entyer signal :").lower()

if signal=="red":

    print("stop")

elif signal=="green":

    print("go...")

elif signal=="yellow":
    print("wait !")

else:
    print("invalid signal")

