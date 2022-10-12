Employee=[{"name":"tina","age":30,"birthday":"1990/03/10","job":"devops engineer","address":{"city":"new york","country":"usa"}},{"name":"tim","age":35,"birthday":"1985/02/21","job":"developer","address":{"city":"sydney","country":"australia"}}]
for r in Employee:
    for s in r:
        if s=="name":
            print(s,"=",r[s])
        elif s=="job":
            print(s,"=",r[s])
        elif s=="city":
            print(s,"=",r[s])
        elif s=="address":
            for t in r[s]:
                if t=="city":
                    print(t,"=",r[s][t])
        else:
            pass
print(Employee[1]["address"]["country"])

OUTPUT:
name = tina
job = devops engineer
city = new york
name = tim
job = developer
city = sydney
australia
