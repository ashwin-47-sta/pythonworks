

arr=[2,3,4,5,7,8,9]

sum=int(input("enter sum :"))

for i in range(0,len(arr)-1):

     for j in range(i+1,len(arr)):

         cur_sum=arr[i]+arr[j]

         if sum==cur_sum:
            print(arr[i],arr[j])

            break



lst=[2,3,4,5]
#12,11,10,0

# sample input
lst=[3,6,7]
#13,10,9

# sample input 3