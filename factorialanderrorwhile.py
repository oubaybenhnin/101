n=int(input("Enter a natural number : "))
while n<0 :
    n=int(input("Enter a valid number : "))
    if n>=0 :
        break
if n==0 :
    print("The factorial of 0 is 1")
else :
    f=1
    for i in range (2,n+1):
        f=f*i
    print("The factorial of ", n ," is : ", f )
