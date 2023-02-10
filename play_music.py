import spotipy
import spotipy.util as util

def play_music(username, playlist_id):
  # Get an access token for the Spotify API
  scope = "user-library-read playlist-read-private"
  client_id = "YOUR_CLIENT_ID_HERE"
  client_secret = "YOUR_CLIENT_SECRET_HERE"
  redirect_uri = "YOUR_REDIRECT_URI_HERE"
  token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

  # Create a Spotify client using the access token
  sp = spotipy.Spotify(auth=token)

  # Get the tracks in the specified playlist
  playlist_tracks = sp.playlist_tracks(playlist_id)["items"]
  track_ids = [track["track"]["id"] for track in playlist_tracks]

  # Add the tracks to the user's library
  sp.current_user_saved_tracks_add(track_ids)

  # Start playing the tracks
  sp.start_playback(uris=track_ids)

