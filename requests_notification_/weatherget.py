# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name CITY = "Hyderabad"
# API key API_KEY = "Your API Key"
# upadting the URL
CITY='Toronto'
API_KEY=r'7ea4a8dd07ab5de2922f018dd83c8a68'
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
with open('input.txt','w') as file:
   file.write(str(URL))
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")
   print(response.status_code)
with open('input.txt','w') as file:
   file.write(f'Temperature: {round(temperature-273.15,2)}°C\n')
   file.write(f"Humidity: {humidity}%\n")
   file.write(f"Pressure: {pressure} hPa\n")
   file.write(f"Weather Report: {report[0]['description']}\n")