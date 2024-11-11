#%%
import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()


    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")
    print()
    fin_players = []
    for player in players:
        if player.nationality == "FIN":
            fin_players.append(player)

    for player in sorted(fin_players,key=lambda player: player.points, reverse=True):
        print(player)



if __name__ == "__main__":
    main()