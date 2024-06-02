import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"cod": "404"}  # Return a custom code for city not found

def display_weather(data, temp_unit='C', speed_unit='m/s'):
    if data["cod"] == "200":
        print("Weather Forecast:")
        for forecast in data["list"]:
            date = forecast["dt_txt"]
            weather_desc = forecast["weather"][0]["description"]
            temp = forecast["main"]["temp"]
            if temp_unit == 'F':
                temp = (temp * 9/5) + 32
            humidity = forecast["main"]["humidity"]
            wind_speed = forecast["wind"]["speed"]
            if speed_unit == 'mph':
                wind_speed = wind_speed * 2.23694
            print(f"Date: {date}")
            print(f"Weather: {weather_desc}")
            print(f"Temperature: {temp}°{temp_unit}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} {speed_unit}")
            print("------------------------")
    elif data["cod"] == "404":
        print("City not found. Please enter a valid city name.")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    temp_unit = input("Enter temperature unit (C/F): ").upper()
    speed_unit = input("Enter wind speed unit (m/s/mph): ").lower()

    # Retrieve API key from environment variable
    api_key = os.getenv("API_KEY")

    weather_data = get_weather(city, api_key)
    display_weather(weather_data, temp_unit, speed_unit)
