import os
import requests
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

def get_weather_icon(description):
    desc = description.lower()
    if 'cloud' in desc:
        return '☁️'
    elif 'rain' in desc:
        return '🌧️'
    elif 'clear' in desc:
        return '☀️'
    elif 'storm' in desc or 'thunder' in desc:
        return '⛈️'
    elif 'snow' in desc:
        return '❄️'
    else:
        return '☁️'

@main.route('/', methods=['GET', 'POST'])   
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = os.getenv('WEATHER_API')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            icon = get_weather_icon(data['weather'][0]['description'])
            weather = {
                "city": city.title(),
                "temp": round(data['main']['temp']),
                "description": data['weather'][0]['description'],
                "icon": icon
            }

    return render_template("index.html", weather=weather)