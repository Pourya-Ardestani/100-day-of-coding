##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime
import smtplib
import os

SENDER_EMAIL = "pouryaarde@gmail.com"
PASSWORD = os.environ.get('PASSWORD')
list_of_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']


def send_email():
    chosen_letter = random.choice(list_of_letters)
    with open(f"letter_templates/{chosen_letter}") as letter:
        sentence = letter.read()
        # print(person['name'])
        sentence = sentence.replace('[NAME]', person['name'])
        # print(sentences+'\n')
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=person['email'],
                            msg=f"Subject:Happy Birthday\n\n{sentence}")


# 1. Update the birthdays.csv
try:
    df = pandas.read_csv('birthdays.csv')
    people_in_list = df.to_dict(orient='records')
except Exception as e:
    print(e)

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
day = now.day
month = now.month

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

for person in people_in_list:
    if day == person['day'] and month == person['month']:
        send_email()
# 4. Send the letter generated in step 3 to that person's email address.
