import requests
import cred
from winotify import Notification, audio

session = requests.session()

url = f"https://api.openweathermap.org/data/2.5/weather?q=Riverside,us&appid={cred.api_key}&units=imperial"
response = session.get(url)

if response.status_code == 200:
    riverside = response.json()
    currentTemp = riverside["main"]["temp"]
    toast = Notification(app_id="windows app",
                        title = "Current weather",
                        msg=f"It is currently {currentTemp}")
    toast.set_audio(audio.Mail, loop=False)
    toast.show()

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
