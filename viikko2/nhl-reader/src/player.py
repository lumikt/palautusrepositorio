class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.points = self.goals+self.assists
    def __str__(self):
        return f'{self.name:20}{self.team:5}{self.goals:4} +{self.assists:4} ={self.points:4}'
