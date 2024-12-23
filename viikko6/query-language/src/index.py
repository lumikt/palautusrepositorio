from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
TEST = True
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = Or(
    HasAtLeast(100, "goals"),
    HasAtLeast(70, "assists")
)
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
