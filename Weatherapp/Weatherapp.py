from flask import Flask, request, render_template
import requests
from datetime import datetime

app = Flask(__name__)

def timestamp_to_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

app.jinja_env.filters['timestamp_to_time'] = timestamp_to_time

@app.route('/', methods=["GET", "POST"])
def index():
    weatherData = ''
    error = ''
    cityName = ''

    if request.method == "POST":
        cityName = request.form.get("cityName")

        if cityName:
            weatherApiKey = 'c1c101618e28a028eae8952587d95124'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={weatherApiKey}"

            try:
                response = requests.get(url)
                response.raise_for_status()
                weatherData = response.json()
            except requests.exceptions.HTTPError as http_err:
                error = f"HTTP error occurred: {http_err}"
            except requests.exceptions.RequestException as req_err:
                error = f"Error: {req_err}"
        else:
            error = "Please enter a valid city name."

    return render_template('index.html', data=weatherData, cityName=cityName, error=error)


@app.route('/details/<cityName>')
def details(cityName):
    try:
        weatherApiKey = 'c1c101618e28a028eae8952587d95124'  # The API key
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={weatherApiKey}"

        # Send a GET request to the OpenWeatherMap API for 5-day forecast
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        forecastData = response.json()  # Extract JSON data from the response

        # Render the template 'details.html' and pass forecast data and cityName to it
        return render_template('details.html', data=forecastData, cityName=cityName, error=None)
    except requests.exceptions.RequestException as e:
        print("Error:", e)  # Print error message
        error = "Could not retrieve weather forecast data. Please try again later."  # Set error message
        return render_template('details.html', data=None, cityName=cityName, error=error)


if __name__ == "__main__":
    app.run(debug=True)
