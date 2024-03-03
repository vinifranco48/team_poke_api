from typing import Dict
from src.models.teams_model import TeamsModel

class GetTeamController:
    def search_team_id(self, id: int) -> Dict:
        team = self.__search_team(id)
        formatted_response = self.__format_response(team)
        
        return formatted_response
        
    def __search_team(self, id: int) -> Dict:
        team_model = TeamsModel()

        team = team_model.get_team(id)

        return team
    
    def __format_response(self, team: Dict) -> Dict:
        formatted_response = {
            "owner": team["owner"],
            "pokemons": team["pokemons"]
        }

        return formatted_response