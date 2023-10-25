import requests

# https://automatetheboringstuff.com/files/rj.txt

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(response.status_code)

print(len(response.text))

print(response.text[:100])

# raise exception if download failed , do nothing if succeeded
response.raise_for_status()

""" badResponse = requests.get('https://automatetheboringstuff.com/files/9879494156459879')

print(badResponse.status_code)

print(len(badResponse.text))

print(badResponse.text[:100])

# raise exception if download failed , do nothing if succeeded
badResponse.raise_for_status() """

play_file = open('romeu_and_juliet.txt', 'a')

play_file.write(response.text)

play_file = open('romeu_and_juliet2.txt', 'wb')

for chunk in response.iter_content(100000):
    play_file.write(chunk)