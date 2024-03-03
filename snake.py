from turtle import Turtle

# Constants for the main numbers of te game
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# direction constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakebody = []
        self.create_snake()
        self.head = self.snakebody[0]
        self.tail =self.snakebody[-1]

    def create_snake(self):
        """Creating the body of the snake for thr first time """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        """Moving the snake forward always by changing the position of te segments"""
        for new_seg in range(len(self.snakebody) - 1, 0, -1):
            new_x = self.snakebody[new_seg - 1].xcor()
            new_y = self.snakebody[new_seg - 1].ycor()
            self.snakebody[new_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        """Create the snake body segments"""
        new_snakebody = Turtle("square")
        new_snakebody.color("white")
        new_snakebody.penup()
        new_snakebody.goto(position)
        self.snakebody.append(new_snakebody)

    def reset(self):
        for seg in self.snakebody:
            seg.goto(1000,1000)
        self.snakebody.clear()
        self.create_snake()
        self.head =self.snakebody[0]

    def extend(self):
        """Addes extra segment to the end on the snake when its called"""
        self.add_segment(self.tail.position())

    # the functions for the control of the snake movement
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
