import tabulate
import requests
import os
from dotenv import load_dotenv
import sys


def main():
    respose_json = api_caller(location_selector())
    formatted_weather = format_weather_data(respose_json)
    display_weather(formatted_weather)
    

def location_selector():
    while True:
        print("Select location method: \n(A) Using IP address\n(B) Typing a location manually")
        user_choice = input("= ").strip().upper()
        if user_choice == "A":
            return "auto:ip"
        elif user_choice == "B":
            location = input("What's the location: ")
            if location == "":
                sys.exit("Error: location can't be empty")
            return location
        else:
            print(f"'{user_choice}' ins't a valid input. Please choose from option A or B")


def api_caller(location):
    load_dotenv()    
    api_key = os.getenv("API_KEY")
    try:
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        sys.exit(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        sys.exit(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        sys.exit(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        sys.exit(f"Unexpected Error: {err}")


def format_weather_data(response):
    try:
        return [
                ["Location", f'{response["location"]["name"]}, {response["location"]["country"]}'],
                ["Time", response["location"]["localtime"]],
                ["Weather", f"{response['current']['temp_c']} celsius"],
                ["Clouds", response["current"]["condition"]["text"]],
                ["Wind", f'{response["current"]["wind_kph"]} km/h'],
                ["Humidity", f'{response["current"]["humidity"]}%'],
                ["Precipitation", f'{response["current"]["precip_in"]}%'],
        ]
    except KeyError as err:
        sys.exit(f"KeyError: the api response doesn't contain the item {err}")


def display_weather(formatted_weather_data):
    print(tabulate.tabulate(formatted_weather_data, tablefmt="grid"))


if __name__ == "__main__":
    main()