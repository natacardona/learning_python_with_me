
from classes.networking import Networking
import pandas as pd

#Create a new instance of networking class sending a URL as parameter
networking = Networking('https://rickandmortyapi.com/api/')

response = networking.locations()
json = response.json()

results = json["results"]


dataframe = pd.DataFrame(results)
print(dataframe)
