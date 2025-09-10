from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.score_overwritten()
        self.hideturtle() #Makes that little arrow (turtle) hidden 
    
    def score_overwritten(self):
        self.write(f'Score : {self.scores}', align = 'center',font = ('Arial','18','normal'))

    def game_over(self):
        self.color('white')
        self.goto(0,0)
        self.write('Game Over', align = 'center',font = ('Fixedsys','18','normal'))

    def trackscore(self):
        self.scores += 1
        self.clear()
        self.score_overwritten()

