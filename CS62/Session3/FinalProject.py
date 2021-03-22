import requests

# Authorization Code Flow: It provides an AUTHORIZATION CODE, ACCESS TOKEN AND REFRESH TOKEN. REFRESH TOKEN
# can be used to request a new ACCESS TOKEN
# STEPS FOLLOWED: https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow

## Have your application request AUTHORIZATION CODE; the user clicks/logs in link and authorizes access
#------------------------------------------------------------------------------------------------------
# authorize_url = "https://accounts.spotify.com/authorize"
# response_type = "code"
# redirect_uri = "http://localhost:8888/callback/"
# client_id = "2e241ce5ac624da8805758aba67d484a"
# client_secret = "48322677b582406cb5389822f6f8de7b"
# params = {"client_id": client_id,
#           "response_type": "code",
#           "redirect_uri": redirect_uri,
#           "scope" : ['user-read-email', 'user-read-private']}
#
# response = requests.get(authorize_url, params = params)
# print(response.url)

#-----------------------------------
## GET REFRESH TOKEN & ACCESS TOKEN
#-----------------------------------
# "code" value is received from Authorization Code URL received from above
request_access_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": 'authorization_code',
        "code": 'AQBqL2qgxEhOWEte8umSuzZoCVv5tfexK48inRxFu05k_nvGGkC01lWD2Dt5T91tAC8enoeH1nzVksZ1BBu6cwJ_FZU9BIZkaYqEK-DhDqTX4SAN-LHvHd1tVYdtj42HpAKG4HkAZ-bpwmyoh1FUEI1A0z8O6oUHwqw6Ix-XN0j41DiItvzRG783XtHNECmbO2HY6w',
        "redirect_uri": "http://localhost:8888/callback/"}

headers = {
    "Authorization": "Basic MmUyNDFjZTVhYzYyNGRhODgwNTc1OGFiYTY3ZDQ4NGE6NDgzMjI2NzdiNTgyNDA2Y2I1Mzg5ODIyZjZmOGRlN2I="}
response_token = requests.post(request_access_url, data=data, headers=headers)

print(response_token.json())
response_data = response_token.json()
refresh_token = response_data["refresh_token"]
access_token = response_data["access_token"]
print(response_data["access_token"])
print(response_data["refresh_token"])

#access_token = 'BQDnohwDFeq7taDXV_3GOhLZucf92zOpnXp9sSeDG3lV1g2Fc46Eo6Tt0mQmwmGm0vpP_6EPH1ZhR62-nPsS6iwO-YXTaDclCE1Z2IZm2avf_x-S51wNDbqk7Q8Fy53cqa3wkogZZyX8OSTSWIvPFFgLhUXYPx3I6nO45_k'
#refresh_token = 'AQAp93inTy7SUNZwbzyyOdVbdNVnbS2YwpJ2reqMe-G32zdHhvHywnBj5Gyd1Jtvif5wnPq54HQzM2oClR_iMyeNzO01JSMxWbi8hFX7AgvC90SYDEK6GU8XtWuRbVwiZ50'
#
# #------------------------------------------
# #### Get a List of Current User's Playlists
#--------------------------------------------
current_user_URL = "https://api.spotify.com/v1/me/playlists"
headers = {'Authorization': f"Bearer {access_token}"}
params = {"user_id": "18ssDv1dzG7vrLl7vCOzm7"}

current_user_list_response = requests.get(current_user_URL, headers = headers, params = params)
print(current_user_list_response.json())

#------------------------------------------------------------------------------------
## Use the access token to access the Spotify Web API; Spotify returns requested data
#------------------------------------------------------------------------------------
# Remove Items from a Playlist
#-----------------------------
# playlist_id = "18ssDv1dzG7vrLl7vCOzm7"
# remove_URL = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
# params = {"Authorization": f"Bearer {access_token}",
#            "scope": 'playlist-modify-public playlist-modify-private',
#   "tracks": [
#     {
#       "uri": "spotify:track:7Dt6y0fd2Zi2rN2YWE2N1a",
#       "positions": [
#         0
#       ]
#     },
#     {
#       "uri": "spotify:track:53Lfqp8F0KCInwcFjabMJB",
#       "positions": [
#         1
#       ]
#     }
#   ],
#            "Accept": "application/json",
#            "Content-Type": "application/json"}
# remove_items_response = requests.delete(remove_URL, params = params)
# print(remove_items_response.status_code)
# print(remove_items_response.json())

#----------------------
# # Getting a Track API
#----------------------
# track_id = "53Lfqp8F0KCInwcFjabMJB" # We can assign a new track_id here
# web_api_url = f"https://api.spotify.com/v1/tracks/{track_id}"
# print(web_api_url)
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": f"Bearer {access_token}"}
#
# album_response = requests.get(web_api_url, headers = headers)
# print(album_response.json())

#---------------------------
# Get a Playlist Cover Image
#---------------------------
headers = {'Authorization': f'Bearer {access_token}'}
playlist_id = "18ssDv1dzG7vrLl7vCOzm7"
cover_URL = f"https://api.spotify.com/v1/playlists/{playlist_id}/images"

cover_image_response = requests.get(cover_URL, headers = headers)
print(cover_image_response.json())

#---------------------------------------
### Upload a Custom Playlist Cover Image
#---------------------------------------
headers = {'Authorization': f'Bearer {access_token}',
           "Content-Type": "image/jpeg",
           "scope": ["ugc-image-upload", "playlist-modify-private", "playlist-modify-public"]}
playlist_id = "18ssDv1dzG7vrLl7vCOzm7"
upload_image_URL = f"https://api.spotify.com/v1/playlists/{playlist_id}/images"
data = {}

upload_image_response = requests.put(upload_image_URL, headers = headers, data = data)
print(upload_image_response.json())

#---------------------------------------------------------------------------------------
# ## Requesting a refreshed access token; Spotify returns a new access token to your app
#---------------------------------------------------------------------------------------
# Got the Authorization code from https://www.base64encode.org/ using client_id:client_secret
# get_access_token_URL = "https://accounts.spotify.com/api/token"
# data = {'content-type': "application/x-www-form-urlencoded",
#         'grant_type': "refresh_token",
#         'refresh_token': refresh_token}
# headers = {"Authorization": "Basic MmUyNDFjZTVhYzYyNGRhODgwNTc1OGFiYTY3ZDQ4NGE6NDgzMjI2NzdiNTgyNDA2Y2I1Mzg5ODIyZjZmOGRlN2I="}
#
# response_access_token = requests.post(get_access_token_URL, data = data, headers = headers)
# response_json = response_access_token.json()
# print(response_access_token.json())
# value = response_json['access_token']
# print(value)
#
# # NOT NEEDED INFO: https://www.urlencoder.org/ FOR URL ENCODING
#

access_token = 'BQD5vT6-nBHKKXcHBOK8KxxjHNbLoxc92b9e9cnBu9LJlbDZxTC0lMwpUiUJ8Tc-t270Xulod6SA7ROZc9MIqZC5x2Hv_OsTR5v_NFVbN0m7FSKd3nAyuw0NCer3_x-8uDauCHadh56OsNeMQNcXAmv7CmjO30_tpWrRloG9kDcDCLMH0QZn2idmGM4S'

#-----------------------------------------
#### DELETE playlist with new access token
#-----------------------------------------
# playlist_id = "18ssDv1dzG7vrLl7vCOzm7"
# remove_URL = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
# params = {"Authorization": f"Bearer {access_token}",
#            "scope": 'playlist-modify-public playlist-modify-private',
#   "tracks": [
#     {
#       "uri": "spotify:track:7Dt6y0fd2Zi2rN2YWE2N1a",
#       "positions": [
#         0
#       ]
#     },
#     {
#       "uri": "spotify:track:53Lfqp8F0KCInwcFjabMJB",
#       "positions": [
#         1
#       ]
#     }
#   ],
#            "Accept": "application/json",
#            "Content-Type": "application/json"}
# remove_items_response = requests.delete(remove_URL, params = params)
# print(remove_items_response.status_code)
# print(remove_items_response.json())