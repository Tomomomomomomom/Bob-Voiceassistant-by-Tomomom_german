import requests

def get_weather():
    # Fetch the current weather from a weather API
    url = "https://api.openweathermap.org/data/2.5/weather?q={YOUR_CITY}&units=metric&appid={YOUR_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Get the temperature and weather description from the response
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    # Return a response with the temperature and weather description
    return f"Das Wetter ist derzeit {temperature} Grad Celsius und {description}."
