import smtplib

my_email = ""
password = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="jarzyna79@poczta.onet.pl", msg="Hello jarzyna")
connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)
print(year)

date_of_birth = dt.datetime(year=1995, month=12, day=7, hour=4)
# print(date_of_birth)


import datetime as dt
import random
import smtplib

now = dt.datetime.now()
current_day = now.weekday()


with open("quotes.txt") as quotes_list:
    quotes = quotes_list.readlines()

random_quotes = random.choice(quotes)


my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="jarzyna79@poczta.onet.pl",
                        msg=f"Subject:Motivational message\n\nThis is a random text from list\n{random_quotes}")




