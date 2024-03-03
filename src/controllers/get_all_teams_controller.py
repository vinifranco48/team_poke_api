from typing import Dict
from src.models.teams_model import TeamsModel

class GetAllTeamController:
    def search_all_teams(self) -> Dict:
        teams = self.__search_teams()
        formatted_response = self.__format_response(teams)
        
        return formatted_response
        
    def __search_teams(self) -> Dict:
        teams_model = TeamsModel()

        teams = teams_model.get_all_teams()

        return teams
    
    def __format_response(self, teams: Dict) -> Dict:
        formatted_response = {}

        for index, team in enumerate(teams, start=1):
            metadata = {}
            metadata["owner"] = team["owner"]
            metadata["pokemons"] = []
            for pokemon in team["pokemons"]:
                pokemon_data = {
                    "id": pokemon["id"],
                    "name": pokemon["name"],
                    "weight": pokemon["weight"],
                    "height": pokemon["height"]
                }
                metadata["pokemons"].append(pokemon_data)
            formatted_response[str(index)] = metadata
            
        return formatted_response