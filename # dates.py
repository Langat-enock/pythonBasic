
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime( "%a, %d-%m-%Y") # day-mount-
print(formatted_date)

after_forty_day  = today+timedelta(days=14)  # crl +click to actual class
print(after_forty_day)
dob = "1990_01- 25"

# convert to date object
date_of_birth = datetime(dob, "%Y-%m-%d")
age = -date_of_birth
print("I am ",age, "years old")

age_in_day =datetime.today() - date_of_birth
print(age_in_day.days)


