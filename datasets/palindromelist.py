def is_palindrome(lst):
    
    return lst == lst[::-1]


my_list = [1, 2, 3, 2, 1]

print(is_palindrome(my_list))