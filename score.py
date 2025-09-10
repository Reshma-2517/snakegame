from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        with open('data.txt') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.score_overwritten()
        self.hideturtle() #Makes that little arrow (turtle) hidden 
    
    def score_overwritten(self):
        self.clear()
        self.write(f'Score : {self.scores} Highscore :{self.highscore}', align = 'center',font = ('Arial','18','normal'))
    
    def restart(self):
        if self.scores > self.highscore:
            self.highscore = self.scores
            with open('data.txt','w') as file:
                file.write(f'{self.highscore}')
        self.scores = 0 #Reset the score 
        self.score_overwritten()
        

    # def game_over(self):
    #     self.color('white')
    #     self.goto(0,0)
    #     self.write('Game Over', align = 'center',font = ('Fixedsys','18','normal'))

    def trackscore(self):
        self.scores += 1
        self.score_overwritten()

