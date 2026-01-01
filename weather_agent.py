import requests
API_KEY = "1488735e05a90b275472c05e1c04f2cd"

def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }