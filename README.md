# WeatherWizzard
A weather app i'm working on with BIgSnake Django
# Weather CLI App

A simple Django-based command-line application to query weather information using the OpenWeather API.

## Setup

1. Make sure you have Python and Django installed
2. Clone this repository
3. Navigate to the project directory
4. Replace the placeholder with your OpenWeather API key in `weather/management/commands/getweather.py`:
   ```python
   # Find this line in getweather.py
   api_key = 'YOUR_API_KEY_HERE'  # Replace with your API key
   ```

   To get an API key:
   1. Sign up at [OpenWeather](https://openweathermap.org/)
   2. Go to your account page
   3. Copy your API key
   4. Replace the placeholder in the code with your own API key

## Usage

To query the weather for a city, use:
```bash
python manage.py getweather "city_name"
```

For example:
```bash
python manage.py getweather "London"
```

This will display:
- Temperature in Celsius
- Humidity percentage
- Weather conditions
- Wind speed in meters per second

## Example Output
```
Weather in London:
Temperature: 15.2°C
Humidity: 76%
Conditions: Partly Cloudy
Wind Speed: 4.1 m/s
```

## Error Handling

The app includes error handling for:
- Invalid city names
- Network connection issues
- API response errors

If you encounter any errors, the app will display a helpful error message indicating what went wrong.
