# import smtplib
#
# my_email = "sadeedakhtar04@gmail.com"
# password = "wcmrfzwegujdhhrl"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # This make the connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="sadeedakhtar03@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")
 

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
#
# date_of_birth = dt.datetime(year=2003 , month=7 , day=27)
# print(date_of_birth)




import smtplib
import datetime as dt
import random

MY_EMAIL = "Sadeedakhtar04@gmail.com"
MY_PASSWORD = "wcmrfzwegujdhhrl"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2: # Monday is 0, and sunday is 6.
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="sadeedakhtar03@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")

#------------------- AUTOMATED BIRTHDAY WISHER PROJECT -------------------