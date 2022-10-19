import pandas as pd
c=pd.read_excel("D:\\emp.xlsx")
df=pd.DataFrame(c)
print(df)
print()
print("after sorting a spread sheet:")
print()
print(df.sort_values("Years of experience",ascending=False))



OUTPUT:
    
faculty Name  Years of experience Subjects
0         Raji                    4    maths
1        Bujji                    2     DBMS
2         Siva                    1       DS
3          Sai                    3     HTML

after sorting a spread sheet:

  faculty Name  Years of experience Subjects
0         Raji                    4    maths
3          Sai                    3     HTML
1        Bujji                    2     DBMS
2         Siva                    1       DS
    
         


  
