# Weather App using Flask in Python

## Overview
This is a simple weather application built using Flask and Python. It fetches real-time weather data from the OpenWeatherMap API and displays it in a user-friendly interface. Users can enter a city name to get current weather details and view a 5-day forecast.

## Features
- Fetches real-time weather data for any city
- Displays temperature, pressure, humidity, wind speed, sunrise, and sunset times
- Provides a 5-day weather forecast
- User-friendly Bootstrap-based UI

## Technologies Used
- Python
- Flask (Web Framework)
- HTML, CSS, Bootstrap (Frontend)
- OpenWeatherMap API

## Installation & Setup
### Prerequisites:
- Python 3.x installed
- Flask installed (`pip install flask`)
- Requests library installed (`pip install requests`)

### Steps to Run the Application:
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the following command to start the Flask server:
   ```bash
   python Weatherapp.py
   ```
4. Open a web browser and go to `http://127.0.0.1:5000/`.

## Project Structure
```
├── Weatherapp.py       # Main Flask application
├── index.html          # Frontend UI template
├── details.html        # Forecast details page (not included in upload)
├── static/             # (If any additional assets like CSS, JS)
```

## API Usage
This project uses the OpenWeatherMap API to fetch weather data. Ensure you replace the API key in `Weatherapp.py` with your own key:
```python
weatherApiKey = 'your_api_key_here'
```

## Contribution
Feel free to fork this repository and make improvements. Pull requests are welcome!

## License
This project is open-source and available under the MIT License.

---
Developed by Yameen Munir

