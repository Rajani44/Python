import pandas as pd
c=pd.read_excel("D:\\raj.xlsx")
df=pd.DataFrame(c)
print(df)
print()
print("after sorting a spread sheet:")
print()
print(df.sort_values("years of experience",ascending=False))


OUTPUT:
    Name  years of experience  Unnamed: 2 subjects
0   Raji                    2         NaN    maths
1  Bujji                    3         NaN     DBMS
2   Siva                    1         NaN       DS
3    Sai                    0         NaN     HTML

after sorting a spread sheet:

    Name  years of experience  Unnamed: 2 subjects
1  Bujji                    3         NaN     DBMS
0   Raji                    2         NaN    maths
2   Siva                    1         NaN       DS
3    Sai                    0         NaN     HTML


  
