# Weather-app

- The code defines a Python program that retrieves and displays weather information using the Weather API.

1. First, the necessary modules are imported, including tabulate, requests, os, load_dotenv, and sys.

2. Then, the main() function is defined, which calls other functions to complete the program's operations. Inside main(), the api_caller() function is called with the location_selector() function as an argument. The returned data from api_caller() is then passed to format_weather_data() function, which formats the data into a 2D list. Finally, display_weather() is called to display the weather data in a formatted table using the tabulate module.

3. The location_selector() function is responsible for allowing the user to choose how to input their desired location, either by using an IP address or typing a location manually. The user's input is checked for validity, and the selected method is returned.

4. The api_caller() function calls the Weather API using the requests module with the location information passed to it. If the request is successful, the JSON response is returned. If there is an error, an appropriate error message is printed with sys.exit().

5. The format_weather_data() function takes the JSON response from api_caller() and extracts the necessary information, formatting it into a 2D list.

6. Finally, the display_weather() function takes the formatted 2D list and displays it in a formatted table using the tabulate module.

- The program's __name__ variable is checked to ensure that it is the main program that is running before the main() function is executed.
