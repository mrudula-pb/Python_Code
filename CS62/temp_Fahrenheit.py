
# Part 5: Print out the current temperature in Fahrenheit for Stanford CA
# hint: Use the 'requests' library to make a 'get' call to the 'url', then use the 'json' library to convert the response
# to something you can sort through like a dictionary
# You'll be looking for 'FeelsLikeF' import requests import json url = 'http://wttr.in/stanford?format=j1'

import requests, json

class Solution:
    def print_dict(self, url):
        response = requests.get(url)
        print(response)
        json_response = response.json()
        # print(json_response['current_condition']['FeelsLikeF']) doesn't work
        print('Current temperature in Fahrenheit for Stanford CA: ' + json_response['current_condition'][0]['FeelsLikeF'])
        # for key, value in json_response.items():
        #     print(str(key) + ":" + str(value))

solution = Solution()
url = 'http://wttr.in/stanford?format=j1'
solution.print_dict(url)