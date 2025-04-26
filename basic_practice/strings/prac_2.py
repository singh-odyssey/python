#replacing elements of template based on user name and current date and time

from datetime import datetime

current_date = datetime.now()
day = current_date.strftime("%A")
year = current_date.year
month = current_date.strftime("%B")
date = current_date.day

template ='''
        Hi <Name>
        Today is <DAY>,<Date> <month>,<YEAR>
'''
name=input("Enter your name -> ")


template = template.replace("<DAY>", day).replace("<YEAR>", str(year)).replace("<Name>", name).replace("<Date>", str(date)).replace("<month>", month)
print(template)