num1=int(input("Enter The first Number: "))
num2=int(input("Enter The Second Number: "))
sign=input("Enter The Sign For The Mathematic operation (In Py Language): ")
if sign == "+" :
    print(str(num1) + sign + str(num2) + " = " + str(num1 + num2))
elif sign == "-" :
    print(str(num1) + sign + str(num2) + " = " + str(num1 - num2))
elif sign == "*" :
    print(str(num1) + sign + str(num2) + " = " + str(num1 * num2))
elif sign == "/" :
    print(str(num1) + sign + str(num2) + " = " + str(num1 / num2))
else :
    print("Try Again, IDIOT.")
