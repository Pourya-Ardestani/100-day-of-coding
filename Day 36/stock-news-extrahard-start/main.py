import os
import smtplib
import datetime
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

SENDER_EMAIL = 'pouryaarde@gmail.com'
EMAIL_PASSWORD = os.environ.get('MY_PASSWORD')
RECEIVER_EMAIL = 'pooryaardestani11@gmail.com'

ALPHAVANTAGE_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

daily_info_end_point = 'https://www.alphavantage.co/query'  # function=TIME_SERIES_DAILY&symbol=IBM&apikey=
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=2)
previous_day = today - datetime.timedelta(days=3)
yesterday_date = str(yesterday.date())
previous_day_date = str(previous_day.date())
# print(f'{yesterday_date} + {previous_day_date}')
# print(type(yesterday_date))

response = requests.get(url=daily_info_end_point, params=parameters)
response.raise_for_status()
days_list = response.json()["Time Series (Daily)"]
# print(days_list)
yesterday_close_market_rise = float(days_list[yesterday_date]['4. close'])
previous_day_close_market_rise = float(days_list[previous_day_date]['4. close'])
print(previous_day_close_market_rise)
print(yesterday_close_market_rise)
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
difference = yesterday_close_market_rise - previous_day_close_market_rise
percentage = round((difference / yesterday_close_market_rise) * 100)
up_down = None
if difference > 0:
    up_down = '🔼'
else:
    up_down = '🔽'

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_parameters = {
    'q': COMPANY_NAME,
    'from': {previous_day_date},
    'to': {yesterday_date},
    'sortBy': 'publishedAt',
    'apiKey': NEWS_API_KEY
}
if abs(percentage > 1 ):
    print("Get News")
    news_to_send = {}
    news_response = requests.get(f'https://newsapi.org/v2/everything', params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    formatted_articles = [
        f"{STOCK}:{up_down}{abs(percentage)}% \nHeadline: {article['title']}. \nBrief:{article['description']}" for article
        in
        three_articles]
    print(formatted_articles)
    print(type(formatted_articles))
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)
        for massage in formatted_articles:
            print(massage)
            print(type(massage))
            server.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=f'Subject:\n\nBody:massage\n\nBcc:AMPou')

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
