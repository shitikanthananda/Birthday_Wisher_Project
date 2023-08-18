import smtplib
import datetime as dt
import random

MY_EMAIL = "udemyshitikanthapython@gmail.com"
PASSWORD = "ijdkawaabzslthyw"

with open("quotes.txt") as file:
    content = file.readlines()
    message = random.choice(content)

now = dt.datetime.now()
week = now.weekday()
if week == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="tirthabasmishra2020@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{message}")
