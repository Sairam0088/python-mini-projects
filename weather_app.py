#Weather app using python

import requests

city = input("Enter a city: ")

url = "http://api.weatherapi.com/v1/current.json?key=7aa2748dcb5246588fd71246242603&q="+city

response = requests.get(url)

data = response.json()

print(f"\nCity: {data["location"]["name"]}")
print(f"Temperature: {data["current"]["temp_c"]} °C")
print(f"Humidity: {data["current"]["humidity"]} %")
print(f"Cloudy: {data["current"]["cloud"]} %\n")