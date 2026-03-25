import requests
import os
import smtplib

OWM_API_KEY = os.environ.get('OWM_API_KEY')

lat = 30.406401
long = -87.682083

api_call = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={OWM_API_KEY}&units=metric"
response = requests.get(url=api_call)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(min(4, len(weather_data['list']))):
    if 500 <= weather_data['list'][i]['weather'][0]['id'] < 600:
        will_rain = True


def send_alert():
    FROM_EMAIL = os.environ.get('FROM_EMAIL')
    To_EMAIL = os.environ.get('TO_EMAIL')
    PASSWORD = os.environ.get('PASSWORD')

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addr=To_EMAIL,
            msg="Subject: Rain Alert\n\nForecast is for rain. Don't forget to take an umbrella."
        )


def all_clear():
    from_email = os.environ.get('FROM_EMAIL')
    to_email = os.environ.get('TO_EMAIL')
    password = os.environ.get('PASSWORD')

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addr=TO_EMAIL,
            msg="Subject: All clear\n\nNo rain forecast for today."
        )


if will_rain:
    send_alert()
else:
    all_clear()




