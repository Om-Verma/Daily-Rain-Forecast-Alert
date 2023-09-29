#hosted on https://www.pythonanywhere.com/ so that we can schedule it everymorning at 7:30AM

import requests  # allows to send HTTP requests using Python
import os
UFO = "https://api.openweathermap.org/data/2.5/forecast"
key = "805b20023ac480ec962bf84a0145a59d"

weather_parameters = {
    "lat": 11.2671,
    "lon": 75.817,
    "appid": key,
    # "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=UFO, params=weather_parameters)
response.raise_for_status()
weather_data=response.json()

will_rain=False         #stores if it is forecasted to rain in the next 12 hrs (3hr period taken)
for i in range(4):
    #print(weather_data["list"][i]["weather"][0]["id"])      # i=1 gives forecast after 3 hours. i=2 after 6 hours and so on
    if(weather_data["list"][i]["weather"][0]["id"]<700):
        will_rain=True

if (will_rain):
    messagee="Get Your Umbrella Ready! Or be prepared to drown in rain! "
else:
    messagee="No need of umbrellas : probably!!"

# Now lets message these results!!
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = 'ACff453c5e2d6f974ae5ba26e49963d090'
auth_token = 'bcb80653c95af4e8dc490ae99a6a9af9'

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

client = Client(account_sid, auth_token,http_client=proxy_client)
message = client.messages.create(
  body=messagee,
  from_='+12565783691',
  to='+916386606214'
)

print(message.status)

