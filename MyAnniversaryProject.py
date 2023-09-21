import datetime as dt
import smtplib
import random

# Emails and password removed for privacy
MY_EMAIL = "myEmail@gmail.com"
HER_EMAIL = "herEmail@gmail.com"
MY_PASS = "weerygfgbdbj"
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

print(quote)
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=HER_EMAIL,
        msg=f"Subject:I love you! <3\n\n{quote}")
