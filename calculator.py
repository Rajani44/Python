count=0
while True:
       num1 = int(input("enter first number: "))
       num2 = int(input("enter second number: "))
       operator = str(input("enter which operation you want:"))
       if operator == "+":
           print("result is:", (num1 + num2))
           count+=1
       elif operator == "-":
           print("result is:", (num1 - num2))
           count+=1
       elif operator == "*":
           print("result is:", (num1 * num2))
           count+=1
       elif operator == "/":
           print("result is:", (num1 / num2))
           count+=1
       r=input('do you want to continue the code:')
       if r=="exit":
           print(count)
           break
       else:
           continue

          
 OUTPUT:
       
enter first number: 4
enter second number: 4
enter which operation you want:*
result is: 16
do you want to continue the code:y
enter first number: 2
enter second number: 8
enter which operation you want:+
result is: 10
do you want to continue the code:y
enter first number: 6
enter second number: 4
enter which operation you want:-
result is: 2
do you want to continue the code:exit
3

 
    
