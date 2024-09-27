import requests
import os
# from twilio.rest import Client

OWP_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get('API_KEY')
account_sid = "ACa24eea0b80bca7aa84926c661a3a7210"
auth_token = os.environ.get('AUTH_TOKEN')

parameters = {
    "lat": 51.507351,
    "lon": -0.127750,
    # 'q' : 'tehran',
    "appid": api_key,
    'exclude': 'hourly'
}
# response = requests.get(
#     url=OWP_Endpoint,
#     params=parameters)
# print(response.status_code)
# response.raise_for_status()
# hole_hours_data = response.json()['hourly']
# first_12_hours = hole_hours_data[:12]
will_rain = True #False
# for hour_data in hole_hours_data:
#     # hour = hole_hours_data[index]
#     for condition in hour_data['weather']:
#         if condition['id'] < 700:
#             will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="don't forget to bring umbrella☔☔☔",
        from_="+12136343225",
        to="+989961201669",
    )
    print(message.status)