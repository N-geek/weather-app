from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import quote_plus
from dotenv import load_dotenv
import requests, os

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Khi production, nên chỉnh domain cụ thể
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_icon(description: str):
    desc = description.lower()
    if 'cloud' in desc: return '☁️'
    if 'rain' in desc: return '🌧️'
    if 'clear' in desc: return '☀️'
    if 'storm' in desc or 'thunder' in desc: return '⛈️'
    if 'snow' in desc: return '❄️'
    return '☁️'

def geocode(address: str):
    """Chuyển địa chỉ → lat/lon bằng Nominatim, ưu tiên kết quả chính xác ở VN"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "addressdetails": 1,
        "limit": 5,
        "accept-language": "vi",
        "countrycodes": ""  # KHÔNG ép buộc country nếu người dùng nhập quốc gia
    }
    headers = {"User-Agent": "weather-app-fastapi"}

    try:
        res = requests.get(url, params=params, headers=headers, timeout=10)
        res.raise_for_status()
        results = res.json()

        # Ưu tiên theo loại địa điểm
        priority_types = ["house", "residential", "road", "village", "town", "city"]
        for ptype in priority_types:
            for r in results:
                if r.get("type") == ptype and "lat" in r and "lon" in r:
                    return float(r["lat"]), float(r["lon"]), r.get("display_name", address)

        if results:
            r = results[0]
            return float(r["lat"]), float(r["lon"]), r.get("display_name", address)

    except Exception as e:
        print(f"[geocode error] {e}")
    return None, None, None

@app.get("/weather")
def weather(
    query: str = Query(default=None, description="Địa chỉ hoặc thành phố"),
    city: str = Query(default=None, description="Tương thích tham số cũ")
):
    api_key = os.getenv("WEATHER_API")
    user_input = query or city
    if not user_input:
        return {"error": "Bạn cần nhập địa chỉ hoặc tên thành phố."}

    print(f"[user_input] {user_input}")

    lat, lon, location_label = geocode(user_input)
    print(f"[geocode] lat={lat}, lon={lon}, location={location_label}")

    if lat is not None and lon is not None:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    else:
        encoded_city = quote_plus(user_input)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}&units=metric"
        location_label = user_input.title()

    print(f"[API call] {url}")

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()

        return {
            "location": location_label or data.get("name", user_input.title()),
            "temp": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"],
            "icon": get_icon(data["weather"][0]["description"])
        }
    except Exception as e:
        print(f"[weather fetch error] {e}")
        return {"error": "Không tìm thấy dữ liệu thời tiết phù hợp"}

@app.get("/health")
async def health():
    return {"status": "ok"}
