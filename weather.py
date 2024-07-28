import requests
import cred
from winotify import Notification

session = requests.session()

url = f"https://api.openweathermap.org/data/2.5/weather?q=Riverside,us&appid={cred.api_key}&units=imperial"
response = session.get(url)


print(response.json())