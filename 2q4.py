#4 Armstrong Number Program In Python
number = int(input("enter the number"))
temp = number
add_sum = 0
while temp!=0:
    k = temp%10
    add_sum +=k*k*k
    temp = temp//10
if add_sum==number:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')
