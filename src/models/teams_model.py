from pymongo import MongoClient
from flask import current_app
from typing import Dict

class TeamsModel:
    def __get_mongo_client(self) -> MongoClient:
        return MongoClient(current_app.config['MONGO_URI'])
    
    def create_teams(self, formatted_response: Dict) -> None:
        with self.__get_mongo_client() as client:
            teams_collection = client.pokemon_database.teams
            last_team = teams_collection.find_one(sort=[('_id', -1)])
            last_id = last_team['_id'] if last_team else 0
            team_data = {"_id": last_id + 1, "owner": formatted_response["owner"], "pokemons": formatted_response["pokemons"]}
            result = teams_collection.insert_one(team_data)
    
    def get_all_teams(self) -> Dict:
        with self.__get_mongo_client() as client:
            teams_collection = client.pokemon_database.teams
            team_data = list(teams_collection.find())

            return team_data  

    def get_team(self, id: int):
        with self.__get_mongo_client() as client:
            teams_collection = client.pokemon_database.teams
            team_data = teams_collection.find_one({"_id": id})
            
            return team_data if team_data else {}