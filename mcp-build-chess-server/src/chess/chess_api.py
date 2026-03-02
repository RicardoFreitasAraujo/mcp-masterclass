import requests

CHESS_API_BASE = "https://api.chess.com/pub"


headers = { "accept":"application/json",
            "User-Agent":"Mozilla/5.0 (Linux; Android 16; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.12.45 Mobile Safari/537.36"}

def get_player_profile(username):
    """Return profile of an username from Chess.com"""
    url = f"{CHESS_API_BASE}/player/{username}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_player_stats(username):
    """Return stats of an username from Chess.com"""
    url = f"{CHESS_API_BASE}/player/{username}/stats"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# if __name__ == "__main__":
#     data = get_player_profile('kikaru')
#     print(data)
