import requests
from typing import Dict

class PokeHandler:

    def search_team(self, team: Dict) -> Dict:
        url_api_poke = 'https://pokeapi.co/api/v2/pokemon/'
        new_team = []

        for pokemon in team:
            response = requests.get(f'{url_api_poke}{pokemon}').json()

            new_team.append({
                "id": response["id"],
                "name": response["name"],
                "weight": response["weight"],
                "height": response["height"]
            })
        
        return new_team
    