
from datetime import datetime
today = datetime.today()
def user_birthday():
    year = int(input("year:"))
    month = int(input("month:"))
    day = int(input("date:"))

    birthday = datetime(year,month,day)
    return birthday
def calculate_dates(birthyday):
    now = datetime.now()
    birthday = datetime(now.year, birthyday.month, birthyday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return (birthday - now.today()).days
    else:
        return (birthday - now.today()).days + 1
bd = user_birthday()
days= calculate_dates(bd)
print("number of days is:", days)
hours = days*24
print("number of hours is:",hours)
minutes = hours*60
print("number of minutes is:", minutes)


OUTPUT:
  
year:2000
month:4
date:4
number of days is: 167
number of hours is: 4008
number of minutes is: 240480
  
  
