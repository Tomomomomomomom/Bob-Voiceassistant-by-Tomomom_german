import requests
import json

def get_recommended_movies():
  # Make a request to the Netflix Roulette API to get a list of recommended movies
  api_url = "https://netflixroulette.net/api/api.php?actor=Tom%20Hanks"
  response = requests.get(api_url)
  data = response.json()

  # Extract the titles of the recommended movies
  movie_titles = [movie["show_title"] for movie in data]

  # Return the titles of the recommended movies
  return movie_titles

