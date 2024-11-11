
class PlayerStats:

    def __init__(self, reader):
        self.players = reader.players
    

    def top_scorers_by_nationality(self, nationality):
        top_scores = []

        for player in self.players:
            if player.nationality == nationality:
                top_scores.append(player)
        
        return sorted(top_scores,key=lambda player: player.points, reverse=True)

    def get_nationalities(self):
        nationalities = ""
        seen = set()
        for player in self.players:
            if player.nationality not in seen:
                nationalities+= f'{player.nationality}/'
                seen.add(player.nationality)
        
        return nationalities