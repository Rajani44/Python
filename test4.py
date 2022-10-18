#printing youngest employee name and age


def get_age(employee):
    return employee.get('age')
employee = [{ "name" : "Tina", "age" : "40", "DoB" : "1990-03-10","job": "Devops Engineer","address":{"city":"New york","country":"USA"}},{ "name" : "Tim", "age" : "35", "DoB" : "1985-02-21","job": "Devoloper","address":{"city":"Sydney","country":"Australia"}}]
employee.sort(key=get_age)
print(employee[0]['name']," ", employee[0]['age'])

#OUTPUT:
Tim   35

#Finding upper and lower case letters in a given string


string= input("enter any string:")
lower= 0
upper= 0
for i in string:
    if(i.islower()):
        lower = lower + 1
    elif(i.isupper()):
        upper= upper + 1
print("The  lower case letters  are:",lower)
print("The  upper case letters are:",upper)


#OUTPUT:

enter any string:Hai GoodMorning
The  lower case letters  are: 11
The  upper case letters are: 3
  
  
#Even number finding:


list=[23,89,76,345,65,8,9,0,5,8]
for i in list:
    if  i%2==0:
        print(i)
        
 #OUTPUT:

76
8
0
8



