
import requests
import json

# Request access token(Bearer token) via Client Credentials Flow
# Client ID c8b3d0665bff4d32b4630cb630152dea
# Client Secret 736caebc8a814ba5a86e86c8cb8a2fb6
# Using Client Credentials Flow:  However that this flow does
# not include authorization and therefore cannot be used to access or to manage a user private data.
# https://community.spotify.com/t5/Spotify-for-Developers/How-to-request-several-scopes-for-a-token-to-Spotify-API/m-p/5070420#M1525
# https://stackoverflow.com/questions/64744170/how-to-request-several-scopes-for-a-token-to-spotify-api

grant_type = 'client_credentials'
CLIENT_ID = 'c8b3d0665bff4d32b4630cb630152dea'
CLIENT_SECRET = '736caebc8a814ba5a86e86c8cb8a2fb6'
body_params = {'grant_type' : grant_type}
url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET))
auth_response_data = response.json()
print(auth_response_data)
access_token = auth_response_data["access_token"]
print(access_token)

# Get a Playlist
print()
print("Get a Playlist: #################")
get_playlist = requests.get("https://api.spotify.com/v1/playlists/18ssDv1dzG7vrLl7vCOzm7", headers={"Authorization": 'Bearer {}'.format(access_token)})
print(get_playlist.json())

# Get a Playlist Cover Image
print()
print("Get a Playlist Cover Image: #################")
get_playlist_image = requests.get("https://api.spotify.com/v1/playlists/18ssDv1dzG7vrLl7vCOzm7/images", headers={"Authorization": 'Bearer {}'.format(access_token)})
print(get_playlist_image.json())
print()
print("Get a Playlist Cover Image: #################")
get_playlist_image = requests.get("https://api.spotify.com/v1/playlists/157VN4bQyM7MNwNNrU8V3T/images", headers={"Authorization": 'Bearer {}'.format(access_token)})
print(get_playlist_image.json())

# TRACKS API
Base_URL = "https://api.spotify.com/v1/"
ids = "7Dt6y0fd2Zi2rN2YWE2N1a,53Lfqp8F0KCInwcFjabMJB,2ywJCXzuC6fJaqdLR4k8F4"
headers = {"Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(access_token)}
track_id = "7Dt6y0fd2Zi2rN2YWE2N1a"
params = {"ids" : ids}
print()
print("Get several TRACKS: #################### ")
get_several_tracks = requests.get(Base_URL + 'tracks', headers = headers, params = params)
print("Get several Tracks: " + str(get_several_tracks.json()))
print("Get Status Code: " + str(get_several_tracks.status_code))

print()
print("Get a Track: #################### ")
get_Track = requests.get(Base_URL + 'tracks/' + track_id, headers = headers)
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

# Library API
print()
print("Get User's Saved Albums: #################### ")
data = {
    "grant_type": "client_credentials",
    "scope": "playlist-modify-private, user-library-read"
}

users_saved_albums = requests.get(Base_URL + "me/albums", headers = headers, data = data)
# print(users_saved_albums.json())
print("Status code of Saved albums: " + str(users_saved_albums.status_code))

# Remove Items from a Playlist
playlist_id = "18ssDv1dzG7vrLl7vCOzm7"
remove_url = "https://api.spotify.com/v1/playlists/18ssDv1dzG7vrLl7vCOzm7/tracks"
data = '{"tracks":[{"uri":"spotify:track:2N6aUazlszu1DDPnSCGifu","positions":[0]},{"uri":"spotify:episode:1au5C4Mj2Gh9RzRD2c92kV","positions":[1]}]}'
print(access_token)
# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer BQDamVKL1ILEIsjegXT6h6XbBsBGd1qphutiFX8vvMM3cmIziiKEWVUbaL_vGQ5RGZHCBfPi5tb6y8VPgm7RhXhU6gKonPWilNytmBiihaUWjmLkt5JzNLE1y_omFRnYZs-R9BopqmDtg7QRqQ-rFHRWMXm3wp-H71f3stm892hBr--utxLbU0elvCdeGjRD_AWk4E60X2cO6QafhnE4bW9yrFLC39qhaJsXWwu8GdAvynkiJe3XaFtZKYiOJ2itTpGd6XSqW_wTsP-HZcBwpDSWhuPLm44trXPDWbcm' }

remove_playlist = requests.delete('https://api.spotify.com/v1/playlists/18ssDv1dzG7vrLl7vCOzm7/tracks', headers={
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(access_token)}, data=data)
print(remove_playlist.status_code)
print(remove_playlist.json())

#params='{"tracks":[{"uri":"spotify:track:1snNAXmmPXCn0dkF9DaPWw"}]}'

#remove=requests.delete("https://api.spotify.com/v1/playlists/55J330mslu8XwOUXef77Qw/tracks",headers=headers,data=params)



# Create a Playlist
print()
print("Create a Playlist: ##################")
user_id = "cs2oscbumd1iyd5zqylk1f8qf"
password = "&k7xgLMU2g)3QjR"
url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
token_new = "BQCvWba5oRmPWz8fefrIiTwPiEbZCSUsEeWlSznGmiCNop6BJvGrQAdyGqNhsbGWjozSeVKV42GSpTDSCLihkt5lNSOywfXegdup3Hw1D94d2AuaxrXntSmT9J2p4JCbxLSKb0uKYtSYN_dq8d9vW1UfcaMJb1FHrY_3hu8OD_KbCDwn58vJsfc3p2Dkq3NI39xLNMQ-v4HycZK_A4CBrMjsO7AgrAc4TxMLK8EtP7cz3sKMq9NcqgvGRDWe6gJt9ilYGmJCoapWLlU9DAQOLdWKJb1dJgiudF9p9gmw"
request_body = json.dumps({
          "name": "Indie bands like Franz Ferdinand but using Python",
          "description": "My first programmatic playlist, yooo!",
          "public": False # let's keep it between us - for now
        })
create_playlist = requests.post(url, headers = {"Content-Type": "application/json", "Authorization": f"Bearer {access_token}"}, data = request_body)
print(create_playlist.status_code)