import googlemaps

# Set your Google Maps API key
API_KEY = "your-api-key"

# Set the origin and destination
origin = "Berlin, Germany"
destination = "Munich, Germany"

# Connect to the Google Maps API
gmaps = googlemaps.Client(key=API_KEY)

# Get the driving directions
directions = gmaps.directions(origin, destination, mode="driving")

# Get the distance and duration of the route
distance = directions[0]["legs"][0]["distance"]["text"]
duration = directions[0]["legs"][0]["duration"]["text"]

# Print the distance and duration
print(f"Distance: {distance}")
print(f"Duration: {duration}")

