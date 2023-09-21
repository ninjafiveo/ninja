import requests
from bs4 import BeautifulSoup
import json

def scrape_weather_data(location):
  """Scrapes the current weather data and the ten day forecast for a given location.

  Args:
    location: The location to scrape the weather data for.

  Returns:
    A dictionary of weather data, including the current weather and the ten day forecast.
  """

  # Make an HTTP request to the weather website.
  response = requests.get(f"https://weather.com/en-US/weather/today/l/{location}")

  # Parse the HTML response.
  soup = BeautifulSoup(response.content, "html.parser")

  # Extract the current weather data.
  current_weather = {}
  current_weather["temperature"] = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text
  current_weather["conditions"] = soup.find("div", class_="CurrentConditions--phraseValue--2Z18W").text

  # Extract the ten day forecast data.
  ten_day_forecast = []
  for day in soup.find_all("div", class_="DailyForecast--card--3a4XU"):
    forecast_day = {}
    forecast_day["date"] = day.find("h3", class_="DailyForecast--date--1YVbc").text
    forecast_day["high_temperature"] = day.find("span", class_="DailyForecast--highTempValue--2q0TW").text
    forecast_day["low_temperature"] = day.find("span", class_="DailyForecast--lowTempValue--144vQ").text
    forecast_day["conditions"] = day.find("div", class_="DailyForecast--conditionsValue--2Z18W").text
    ten_day_forecast.append(forecast_day)

  # Return a dictionary of weather data, including the current weather and the ten day forecast.
  return {
    "current_weather": current_weather,
    "ten_day_forecast": ten_day_forecast
  }

def main():
  """Scrapes the weather data for the specified location and prints the results."""

  # Get the location from the user.
  location = input("Enter a location: ")

  # Scrape the weather data.
  weather_data = scrape_weather_data(location)

  # Print the current weather data.
  print("Current weather for {}:".format(location))
  print("Temperature:", weather_data["current_weather"]["temperature"])
  print("Conditions:", weather_data["current_weather"]["conditions"])

  # Print the ten day forecast data.
  print("Ten day forecast for {}:".format(location))
  for day in weather_data["ten_day_forecast"]:
    print(day["date"], day["high_temperature"], day["low_temperature"], day["conditions"])

if __name__ == "__main__":
  main()
