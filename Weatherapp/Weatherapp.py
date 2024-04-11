from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiKey = 'c1c101618e28a028eae8952587d95124'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + weatherApiKey
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
                weatherData = response.json()
            except requests.exceptions.RequestException as e:
                print("Error:", e)
                error = 1
        else:
            error = 1
    return render_template('index.html', data=weatherData, cityName=cityName, error=error)

if __name__ == "__main__":
    app.run(debug=True)
