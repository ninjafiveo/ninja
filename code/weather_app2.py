import requests
from bs4 import BeautifulSoup
## TEST
def scrape_weather_data(city):
    # URL of the weather website
    # url = f"https://www.wunderground.com/weather/us/oh/youngstown{44512}"
    url = f"https://www.wunderground.com/weather/us/oh/youngstown/44512"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the current weather conditions
        current_weather = soup.find('div', class_='CurrentConditions--currentWeather--3_6KQ')
        
        if current_weather:
            temperature = current_weather.find('span', class_='CurrentConditions--tempValue--1RYJJ').text
            condition = current_weather.find('div', class_='CurrentConditions--phraseValue--2xXSr').text

            print(f"Current Weather in {44512}:")
            print(f"Temperature: {temperature}")
            print(f"Condition: {condition}\n")
        else:
            print(f"Current weather data not found for {44512}.")

        # Extract the 10-day forecast
        forecast = soup.find('div', class_='DailyForecast--DisclosureList--ZQ2qA')
        
        if forecast:
            days = forecast.find_all('div', class_='DailyContent--daypartDate--3MM0J')
            conditions = forecast.find_all('span', class_='DailyContent--narrative--3AcXd')

            print("10-Day Forecast:")
            for day, condition in zip(days, conditions):
                print(f"{day.text}: {condition.text}")
        else:
            print(f"10-day forecast data not found for {44512}.")
    else:
        print(f"Failed to retrieve data for {44512}.")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    scrape_weather_data(city_name)