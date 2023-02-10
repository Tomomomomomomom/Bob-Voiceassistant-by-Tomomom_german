
import requests

def get_news():
    # Fetch the latest news from a news API
    url = "https://newsapi.org/v2/top-headlines?country=de&apiKey={YOUR_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Get the first article from the list of articles
    article = data["articles"][0]
    title = article["title"]
    description = article["description"]

    # Return a response with the title and description of the article
    return f"Die neueste Nachricht ist: {title}. {description}"