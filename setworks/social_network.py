

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]
sanju_followers=["sanju","rohit","kohli"]
   


rahul_folow_suggestions=set(users).difference(set(rahul_followers))

print(rahul_folow_suggestions)

mutual_followers=set(rahul_followers).intersection(set(sanju_followers))
print(mutual_followers)
