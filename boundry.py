from turtle import Turtle

BOX_BOUNDRY = 300

class Boundry(Turtle):

    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.draw()

    def draw(self):
        self.goto(-BOX_BOUNDRY,BOX_BOUNDRY)
        self.pendown()
        self.goto(BOX_BOUNDRY,BOX_BOUNDRY)
        self.goto(BOX_BOUNDRY,-BOX_BOUNDRY)
        self.goto(-BOX_BOUNDRY,-BOX_BOUNDRY)
        self.goto(-BOX_BOUNDRY,BOX_BOUNDRY)


