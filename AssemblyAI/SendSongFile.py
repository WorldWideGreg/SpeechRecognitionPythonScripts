import requests

filename = "Your_Song.mp3"


def read_file(filename, chunk_size=55242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


headers = {'authorization': "YOUR_API_KEY"}
response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))

print(response.json())
