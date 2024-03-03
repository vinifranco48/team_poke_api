from typing import Dict
from src.drivers.poke_handler import PokeHandler
from src.models.teams_model import TeamsModel

class RegisterTeamsController:
    def search_and_register(self, user: str, team: Dict) -> Dict:
        new_team = self.__search(team)
        formatted_response = self.__format_response(user, new_team)
        id = self.__register(formatted_response)
        formatted_response["id"] = id

        return formatted_response

    def __search(self, team:Dict) -> Dict:
        poke_handler = PokeHandler()

        new_team = poke_handler.search_team(team)
        
        return new_team

    def __register(self, formatted_response: Dict) -> int:
        teams_model = TeamsModel()
        
        id = teams_model.create_teams(formatted_response)

        return id
    
    def __format_response(self, user: str, new_team: Dict) -> Dict:
        return { 
            "owner": user,
            "pokemons": new_team
        }





