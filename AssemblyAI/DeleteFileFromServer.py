import requests
headers = {'authorization': "API_KEY_HERE",
           'content-type': "application/json"
           }

response = requests.delete(
    'https://api.assemblyai.com/v2/transcript/ENDOFURL', headers=headers)
print(response.json())
