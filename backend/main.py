from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests, os

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update for production
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_icon(description):
    desc = description.lower()
    if 'cloud' in desc: return '☁️'
    if 'rain' in desc: return '🌧️'
    if 'clear' in desc: return '☀️'
    if 'storm' in desc or 'thunder' in desc: return '⛈️'
    if 'snow' in desc: return '❄️'
    return '☁️'

@app.get("/weather")
def weather(city: str = Query(...)):
    api_key = os.getenv("WEATHER_API")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return {
            "city": city.title(),
            "temp": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "icon": get_icon(data["weather"][0]["description"])
        }
    return {"error": "City not found"}
