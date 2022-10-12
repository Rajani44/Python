Employee={"name":"tim", "age":30, "birthday":"1990/03/10", "job":"Devops Engineer"}
del Employee["age"]
for j in Employee:
    print(j,":",Employee[j])
    
    
 OUTPUT:
 name : tim
birthday : 1990/03/10
job : Devops Engineer
