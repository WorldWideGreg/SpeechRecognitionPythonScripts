import requests


endpoint = "https://api.assemblyai.com/v2/transcript/END_OF_URL"
headers = {
    "authorization": "API_KEY_HERE",
}
response = requests.get(endpoint, headers=headers)
print(response.text)

with open("monfichier.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
