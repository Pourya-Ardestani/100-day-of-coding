# import smtplib
#
my_email = "pouryaarde@gmail.com"
to_email = "pooryaardestani11@gmail.com"
my_password = "jaoomwghecxrsssj"
# subject = "Hal Ahval?"
# body = "dadash khoby che khabar ?"
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:{subject}\n\n{body}")

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
day = now.weekday()
if day == 4:
    with open("quotes.txt") as file:
        lines = file.readlines()
        one_quote = random.choice(lines)
        print(one_quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(my_email,password=my_password)
        server.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:quote of fridays\n\n{one_quote}")
else:
    print("today is not Friday")