import requests
import datetime
import smtplib
import time
import os
MY_LAT = 32.654629
MY_LNG = 51.667984
MY_EMAIL = "pouryaarde@gmail.com"
MY_PASSWORD = os.environ.get('MY_PASSWORD')


def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True
    else:
        return False


parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
    'tzid': 'iran'
}


def is_iss_visible():
    sunrise_response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    sunrise_response.raise_for_status()
    sun_data = sunrise_response.json()
    sunset = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])
    sunrise = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
    hour_now = datetime.datetime.now().hour
    if sunset <= hour_now or hour_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_iss_visible() and is_iss_overhead():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS is near\n\n wake up")
