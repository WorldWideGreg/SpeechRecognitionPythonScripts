import requests

endpoint = "https://api.assemblyai.com/v2/transcript"
json = {"audio_url":  'https://cdn.assemblyai.com/upload/ENDOFURL',
        "language_code": "fr"
        }
headers = {
    "authorization": "API_KEY_HERE",
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())
