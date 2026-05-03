import requests
from dotenv import load_dotenv
load_dotenv()
import  os


api_key = os.getenv('WEATHER_API_KEY')
city = "Rawalpindi"

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)
data = response.json()




# print("City:", data["location"]["region"])
# print("City:", data["location"]["country"])
#
#
# print("Location:", data["location"]["name"])
# print("Local Time:", data["location"]["localtime"])
# print("Temperature:", data["current"]["temp_c"])


