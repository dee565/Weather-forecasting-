from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Get a free API key from https://openweathermap.org/api
API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        elif API_KEY == "YOUR_API_KEY_HERE":
            error = "Add your OpenWeatherMap API key in app.py before searching."
        else:
            try:
                response = requests.get(
                    BASE_URL,
                    params={"q": city, "appid": API_KEY, "units": "metric"},
                    timeout=10
                )
                data = response.json()

                if response.status_code == 200:
                    weather = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "humidity": data["main"]["humidity"],
                        "wind": round(data["wind"]["speed"], 1),
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                    }
                elif response.status_code == 404:
                    error = "City not found. Check the spelling and try again."
                else:
                    error = data.get("message", "Unable to get weather data.")
            except requests.RequestException:
                error = "Could not connect to the weather service. Check your internet connection."

    return render_template("index.html", weather=weather, error=error, city=city)


if __name__ == "__main__":
    app.run(debug=True)
