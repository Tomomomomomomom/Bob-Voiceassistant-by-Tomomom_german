import requests
import json

def search_wikipedia(query):
  # Make a request to the Wikipedia API to search for articles matching the specified query
  api_url = f"https://de.wikipedia.org/w/api.php?action=query&format=json&list=search&utf8=1&formatversion=2&srsearch={query}"
  response = requests.get(api_url)
  data = response.json()

  # Extract the first matching article from the API response
  article = data["query"]["search"][0]
  title = article["title"]
  excerpt = article["snippet"]

  # Make a request to the Wikipedia API to get the content of the article
  api_url = f"https://de.wikipedia.org/w/api.php?action=query&format=json&utf8=1&formatversion=2&prop=extracts&exintro=1&explaintext=1&titles={title}"
  response = requests.get(api_url)
  data = response.json()

  # Extract the content of the article
  page = data["query"]["pages"][0]
  content = page["extract"]

  # Return the title, excerpt, and content of the article
  return (title, excerpt, content)

