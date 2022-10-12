num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
operator=str(input("enter which operation you want:"))
if operator=="+":
    print("result is:", (num1+num2))
elif operator=="-":
    print("result is:", (num1-num2))
elif operator == "*":
    print("result is:", (num1*num2))
elif operator=="/":
    print("result is:", (num1/num2))
else:
    print("you have not typed a valid operator, please run the program again ")
    
    
OUTPUT:
enter first number: 4
enter second number: 40
enter which operation you want:%
you have not typed a valid operator, please run the program again 


enter first number: 20
enter second number: 20
enter which operation you want:*
result is: 400

