##studentclass##

class student:
    def data(self,firstname,lastname,age,lectures):
       self.firstname=firstname
       self.lastname=lastname
       self.age=age
       self.lectures=lectures
    def display(self):
        print(self.firstname,"",self.lastname)
        print(self.lectures)
        v=input("add new lectures:",)
        (self.lectures).append(v)
        print(self.lectures)
        m= list(map(str, input("enter lecture:", ).split()))
        for i in m:
            if i in self.lectures:
                (self.lecture).remove(i)
            else:
                print("not in list")
        print(self.lectures)
s=student()
c=list(map(str,input("enter lecture:",).split()))
s.data("Murali","Mohan",56,c)
s.display()



##output##

enter lecture:telugu english
murali Mohan
['telugu', 'english']
add new lectures:chemistry
['telugu', 'english', 'chemistry']
enter lecture:english
['telugu', 'chemistry']




##professorclass##

class professor:
    def data(self,firstname,lastname,age,subjects):
       self.firstname=firstname
       self.lastname=lastname
       self.age=age
       self.subjects=subjects
    def display(self):
        print(self.firstname,"",self.lastname)
        print(self.subjects)
        a=input("add new subjects:",)
        (self.subjects).append(a)
        print(self.subjects)
        m= list(map(str, input("enter subject:", ).split()))
        for j in m:
            if j in self.subjects:
                (self.subjects).remove(j)
            else:
                print("not in list")
        print(self.subjects)
k=professor()
b=list(map(str,input("enter subject:",).split()))
p=input("enter first name:")
v=input("enter second name:")
n=input("enter the age:")
k.data(p,v,n,b)
k.display()


##output##

enter subject:maths physics
enter first name:Mohan
enter second name:Kumar
enter the age:39
Mohan  Kumar
['maths', 'physics']
add new subjects:chemistry
['maths', 'physics', 'chemistry']
enter subject:maths
['physics', 'chemistry']





##lectureclass##

class lecture:
    def data(self,name,max number of students,duration,list of professors giving this lecture):
       self.n=name
       self.m=max number of students
       self.d=duration
       self.l=list of professors giving this lecture
    def display(self):
        print(self.n)
        print(self.d)
        r=list(map(str,input("adding professor to the list of professors giving this lecture:").split()))
        for i in r:
            (self.l).append(i)
        print(self.l)
       
k=lecture()
n,p=input("name and duration of lecture:")
m=input("max num:",)
a=list(map(str,input("list of professors giving this lecture:").split()))
k.data(n,m,p,a)
k.display()



##output##

name and duration of lecture:maths 3months
max num: 56
listofprofessorsgivingthislecture: sai sam
maths
3months
adding professor to the list of professors giving this lecture:mani sreekanth
['sai','sam','ram','siva']




##students and professors##


class student:
    def data(self,firstname,lastname,age):
       self.firstname=firstname
       self.lastname=lastname
       self.age=age

    def display(self):
        print(self.firstname,"",self.lastname)
        print(self.age)
d=student()
d.data("Murali","Mohan",56,)
d.display()
class professor(student):
    pass
p=professor()
p.data("Anil","Kumar",49)
p.display()



##output##

Murali  Mohan
56
Anil Kumar
49
