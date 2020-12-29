import requests

episodes="https://www.breakingbadapi.com/api/episodes/1"

response = requests.get(episodes)
datos = response.json()
print("Fecha de lanzamiento:",datos[-1]['air_date'])
print("Titulo:",datos[-1]['title'])
print("Episodio:",datos[-1]['episode'])

