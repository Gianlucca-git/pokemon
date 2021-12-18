import requests
from random import randrange

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_pokemon_list(params={}):
    response = generate_request('https://pokeapi.co/api/v2/pokedex/national', params)
    
    pokemonListName = []
    if response:
       pokemonList = response.get('pokemon_entries')

       for value in pokemonList:
           pokemonListName.append(value.get('pokemon_species').get('name'))

       return pokemonListName

    return pokemonListName

def get_pokemon_data(pokemonName):
    response = generate_request('https://pokeapi.co/api/v2/pokemon/' + pokemonName)
    
    pokemonListName = []
    if response:
        pokemonListName = response.get('moves')
    else:
        return pokemonListName

    pokemonUrlMoves= []
    i=0
    listRamdons=[]
    while i<4:
        
        intRamdon= randrange(len(pokemonListName)-1)
        if intRamdon in listRamdons:
            continue
        
        listRamdons.append(intRamdon)
        pokemonUrlMoves.append(pokemonListName[listRamdons[i]].get('move').get('url'))
        
        i+=1 

    return pokemonUrlMoves

def get_moves_data(url):
    response = generate_request(url)

    if response:

        nombre = response.get('name')
        danio  = response.get('accuracy')

        if danio is not None :
            return [nombre,danio]
        else:
            return [nombre,'25']
    
    return ['Generico','25']

    