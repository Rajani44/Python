my_list=[1,2,2,4,4,5,6,8,10,13,22,35,52,83]
m=[]
for s in my_list:
    if s>=10:
        m.append(s)
print(m)
i=[]
n=int(input("enter the number:"))
for r in my_list:
    if r>n:
        i.append(r)
print(i)

OUTPUT:
[10, 13, 22, 35, 52, 83]
enter the number:10
[13, 22, 35, 52, 83]
