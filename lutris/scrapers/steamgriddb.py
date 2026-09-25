import requests
import keyring
import difflib

def get_api_key():
    return keyring.get_password("fabuloutris", "sgdb_api_key")

def search_game(name):
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    return requests.get(f"https://www.steamgriddb.com/api/v2/search/autocomplete/{name}", headers=headers).json()

def find_best_match(game_name, results):
    best_match = None
    best_score = 0
    for game in results["data"]:
        current_score = difflib.SequenceMatcher(None, game_name, game["name"]).ratio()
        if best_score < current_score:
            best_score = current_score
            best_match = game
    return best_match