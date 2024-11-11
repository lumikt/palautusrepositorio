#%%
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from playerreader import PlayerReader
from playerstats import PlayerStats

def main2():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    print("NHL statistics by nationality")
    print()
    season = Prompt.ask("Season:", choices = seasons)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.get_nationalities()
  
    while True:
        print()
        nationality = Prompt.ask("Nationality:", choices= nationalities)
        
        table = Table(title=f"Top scorers {nationality} of season {season}")

        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Team", style="magenta")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Points", justify="right", style="green")
        
        players = stats.top_scorers_by_nationality(nationality)

        for player in players:
            table.add_row(player.name, player.team, str(player.assists), str(player.goals), str(player.points))
        print()
        print(table)
if __name__ == "__main__":
    main2()