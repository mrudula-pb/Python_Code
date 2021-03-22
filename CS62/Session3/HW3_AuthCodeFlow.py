
# Authorization Code Flow

import requests
import base64
import json
from secrets import *

# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}
CLIENT_ID = 'c8b3d0665bff4d32b4630cb630152dea'
CLIENT_SECRET = '736caebc8a814ba5a86e86c8cb8a2fb6'

# Encode as Base64
message = f"{CLIENT_ID}:{CLIENT_SECRET}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')

headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

response = requests.post(url, headers=headers, data=data)

token = response.json()['access_token']

# Step 2 - Use Access Token to GET A PLAYLIST: https://developer.spotify.com/documentation/web-api/reference/#category-playlists
print()
print("Get a PLaylist: ###############")
playlistUrl = f"https://api.spotify.com/v1/playlists/18ssDv1dzG7vrLl7vCOzm7"
headers = {
    "Authorization": "Bearer " + token
}

playlistUrl_response = requests.get(url=playlistUrl, headers=headers)

print(json.dumps(playlistUrl_response.json(), indent=2))


# Get a Playlist Cover Image
print()
print("Get a Playlist Cover Image: #################")
get_playlist_image = requests.get("https://api.spotify.com/v1/playlists/18ssDv1dzG7vrLl7vCOzm7/images", headers = headers)
print(get_playlist_image.json())
print()
print("Get a Playlist Cover Image: #################")
get_playlist_image = requests.get("https://api.spotify.com/v1/playlists/157VN4bQyM7MNwNNrU8V3T/images", headers = headers)
print(get_playlist_image.json())

# TRACKS API
Base_URL = "https://api.spotify.com/v1/"
ids = "7Dt6y0fd2Zi2rN2YWE2N1a,53Lfqp8F0KCInwcFjabMJB,2ywJCXzuC6fJaqdLR4k8F4"
tracks_headers = {"Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token}
track_id = "7Dt6y0fd2Zi2rN2YWE2N1a"
params = {"ids" : ids}
print()
print("Get several TRACKS: #################### ")
get_several_tracks = requests.get(Base_URL + 'tracks', headers = tracks_headers, params = params)
print("Get several Tracks: " + str(get_several_tracks.json()))
print("Get Status Code: " + str(get_several_tracks.status_code))

print()
print("Get a Track: #################### ")
get_Track = requests.get(Base_URL + 'tracks/' + track_id, headers = tracks_headers)
print("Get a Track: " + str(get_Track.json()))
print("Get Track Status Code: " + str(get_Track.status_code))

# print()
# print("Get Audio Features for Several Tracks: #################### ")
# audio_features_several_tracks = requests.get(Base_URL + "audio-features/", headers = headers, params = params)
# print(audio_features_several_tracks.json())
# print('Status Code of Audio features for several Tracks: ' + str(audio_features_several_tracks.status_code))
#
# print()
# print("Get Audio Features for a Track: #################### ")
# audio_features_response = requests.get(Base_URL + "audio-features/" + track_id, headers = headers)
# print(audio_features_response.json())
# print('Status Code of Audio features of a Track: ' + str(audio_features_response.status_code))
#
# print()
# print("Get Audio Analysis for a Track: #################### ")
# audio_analysis = requests.get(Base_URL + 'audio-analysis/' + track_id, headers = headers)
# print(audio_analysis.json())
# print('Status code of audio analysis: ' + str(audio_analysis.status_code))

# ALBUMS API
print()
print("Get User's Saved Albums: #################### ")
albums_headers = {"Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    "scope": "user-library-read"
}

get_saved_albums = requests.get(Base_URL + "me/albums", headers = albums_headers, params = params)
print(get_saved_albums.json())
print("Status code of Saved albums: " + str(get_saved_albums.status_code))

print()
print("Save Albums for Current User: ########")
albums_headers = {"Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    "scope": "user-library-modify, user-library-read"
}

save_albums = requests.put(Base_URL + "me/albums", headers = albums_headers, params = params)
print(save_albums.json())
print("Status code of Saved albums: " + str(save_albums.status_code))

# PLAYLIST API
# Create a Playlist
print()
print("Create a Playlist: ##################")
user_id = "cs2oscbumd1iyd5zqylk1f8qf"
password = "&k7xgLMU2g)3QjR"
url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

# This api works when we use token generated from spotify web console: https://developer.spotify.com/documentation/web-api/reference/#endpoint-create-playlist
token_new = "BQByjnrJTnLOktaxgkTiUNCdnolgq151yU_Xcy2hgiV_A7aUo2gREvKkLrrT5g3TyZ3ORIPXK_Is75jaCN-bGxis8XET36riY_NrcUJ2mH0oJUWJu1qE7dSxbBDyg8OQngh6eFI6l8M1aYA3iE2i83QhlYTZpyyrx7hxMpj_l6d8qeNVR2h_uSEvRXbvLKq0bPZuVmv4-hwP4Py02tnUI6WFyRjqR9Bqw_rHhrqO39D1O_eMEN-qTB1GW2v0Q4QZLgZdR_oW-n7obUJWuvFzlUKKt5FpjuLkkymQhGT8"

playlist_headers = {"Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token_new,
    "scope": "playlist-modify-public"}
request_body = json.dumps({
          "name": "Hello Python",
          "description": "My first programmatic playlist, yooo!",
          "public": True,
          "collaborative": False
        })
create_playlist = requests.post(Base_URL + "users/" + user_id + "/playlists", headers = playlist_headers, data = request_body)
print(create_playlist.status_code)