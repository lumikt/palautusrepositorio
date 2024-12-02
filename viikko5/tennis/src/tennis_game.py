class TennisGame:
    def __init__(self, player1:str , player2:str):
        self.player1 = player1
        self.player2 = player2
        
        self.player1_points = 0
        self.player2_points = 0
        self.score_dictionary = {0: "Love", 1: "Fifteen", 2:"Thirty", 3:"Forty"}

    
    
    def won_point(self, player_name):
        if player_name == self.player1:
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1


    def get_score(self):
        if self.player1_points == self.player2_points:
            score = self.even_scores_string()
        
        elif self.player1_points >= 4 or self.player2_points >= 4:
            score = self.end_game_point_strings()
        else:
            score = f'{self.score_dictionary[self.player1_points]}-{self.score_dictionary[self.player2_points]}'

        return score


    def even_scores_string(self):
        if self.player1_points >= 3:
            score = "Deuce"
        elif self.player1_points < 3:
            score = f'{self.score_dictionary[self.player1_points]}-All'
        
        return score


    def end_game_point_strings(self):
        point_difference = self.player1_points - self.player2_points

        if point_difference == 1:
            score = f'Advantage {self.player1}'
        elif point_difference == -1:
            score = f'Advantage {self.player2}'
        elif point_difference >= 2:
            score = f'Win for {self.player1}'
        else:
            score = f'Win for {self.player2}'
        
        return score