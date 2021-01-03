import requests
from matplotlib import pyplot

url="https://api.covid19api.com/total/dayone/country/Mexico"

response = requests.get(url)

datos = response.json()
confirmados = [dato['Confirmed']for dato in datos]

pyplot.plot(confirmados)
pyplot.title('Casos de Covid-19 En Mexico')
pyplot.style.use('dark_background')
pyplot.show()

print("Fecha",datos[-1]['Date'])