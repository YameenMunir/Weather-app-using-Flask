from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    # Initialize variables
    weatherData = ''  # Variable to store weather data
    error = 0  # Flag to indicate if there's an error
    cityName = ''  # Variable to store the city name
    
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        cityName = request.form.get("cityName")  # Get the city name from the form
        
        # Check if a city name was provided
        if cityName:
            weatherApiKey = 'c1c101618e28a028eae8952587d95124'  # The API key
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + weatherApiKey
            
            try:
                # Send a GET request to the OpenWeatherMap API
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
                weatherData = response.json()  # Extract JSON data from the response
            except requests.exceptions.RequestException as e:
                print("Error:", e)  # Print error message
                error = 1  # Set error flag
        else:
            error = 1  # Set error flag if no city name was provided
    
    # Render the template 'index.html' and pass data to it
    return render_template('index.html', data=weatherData, cityName=cityName, error=error)

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
