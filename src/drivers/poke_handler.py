import requests
from typing import Dict
from src.errors.error_types.http_not_found import HttpNotFoundError

class PokeHandler:

    def search_team(self, team: Dict) -> Dict:
        url_api_poke = 'https://pokeapi.co/api/v2/pokemon/'
        new_team = []
        try:
            for pokemon in team:
                
                response = requests.get(f'{url_api_poke}{pokemon}').json()

                new_team.append({
                    "id": response["id"],
                    "name": response["name"],
                    "weight": response["weight"],
                    "height": response["height"]
                })
        except:
            raise HttpNotFoundError(f"Pokémon {pokemon} not found!!")

        return new_team
    