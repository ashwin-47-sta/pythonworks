

arr=[10,8,7,13,20,25]

arr.sort()


search_element=int(input("enter number:"))

is_present=False

low=0

upper=len(arr)-1

while(low<=upper):

    mid=(low+upper)//2

    if search_element==arr[mid]:

        is_present=True
        break

    elif search_element<arr[mid]:

        upper=mid-1

    elif search_element>arr[mid]:

        low=mid+1

print(is_present)