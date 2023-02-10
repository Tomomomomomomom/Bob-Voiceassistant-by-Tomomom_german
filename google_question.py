import requests
from bs4 import BeautifulSoup

def google_question(query):
  # Make a request to the Google search page with the specified query
  google_url = f"https://www.google.com/search?q={query}"
  response = requests.get(google_url)
  html = response.text

  # Use Beautiful Soup to extract the first search result
  soup = BeautifulSoup(html, "html.parser")
  result = soup.find("div", {"class": "g"})

  # Extract the title and URL of the search result
  title = result.find("h3").text
  url = result.find("a")["href"]

  # Return the title and URL of the search result
  return (title, url)

