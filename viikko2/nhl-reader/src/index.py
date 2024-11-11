#%%
from rich import print as rprint
from playerreader import PlayerReader
from playerstats import PlayerStats

def main2():
   
    rprint("[italic red]Hello[/italic red] World!", locals())
    print("NHL statistics by nationality")
    print()
    season = input('Select season: ')
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.get_nationalities()

    while True:
        nationality = input(f'[pink]{nationalities}[/pink]: ')
        
        if nationality == "":
            break
        players = stats.top_scorers_by_nationality(nationality)

        for player in players:
            print(player)

if __name__ == "__main__":
    main2()