import requests as req

r = req.get(url="https://pokeapi.co/api/v2/pokemon/1")
print(r.content)