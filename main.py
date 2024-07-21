import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LNG = -0.127758



parameters = {
    "Lat": MY_LAT,
    "Lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=51.507351&lng=-0.127758&formatted=0", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


print(f"Sunrise time: {sunrise}")
print(f"Sunset time: {sunset}")

time_now = datetime.now().hour
print(f"Current time: {time_now}")
