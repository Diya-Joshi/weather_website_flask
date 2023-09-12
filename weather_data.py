import requests

def get_weather_data(city):
    API_KEY = '1b1db12eb60889083e97bfd607ab24e2'

    #weather data from OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        print("Weather Data:", weather_data) 
        return weather_data
    else:
        error_message = data['message']
        print("API Error:", error_message)  
        return None


