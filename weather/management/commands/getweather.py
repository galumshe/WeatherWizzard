import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Get weather information for a city using OpenWeather API'

    def add_arguments(self, parser):
        parser.add_argument('city', type=str, help='City name')

    def handle(self, *args, **options):
        city = options['city']
        api_key = '7d4e9161adccddf1ae30d3e0d501a291'

        # OpenWeather API endpoint
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Extract weather information
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']

            # Display weather information
            self.stdout.write(self.style.SUCCESS(f'\nWeather in {city.title()}:'))
            self.stdout.write(f'Temperature: {temp}°C')
            self.stdout.write(f'Humidity: {humidity}%')
            self.stdout.write(f'Conditions: {description.title()}')
            self.stdout.write(f'Wind Speed: {wind_speed} m/s\n')

        except requests.exceptions.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Error fetching weather data: {str(e)}'))
        except KeyError as e:
            self.stderr.write(self.style.ERROR(f'Error parsing weather data: {str(e)}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
