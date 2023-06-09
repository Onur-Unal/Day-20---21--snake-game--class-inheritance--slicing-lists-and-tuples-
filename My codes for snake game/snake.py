from turtle import Turtle

starting_positions = [(0, 0), (-10, 0), (-20, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def move(self):
        for square_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[square_num - 1].xcor()
            new_y = self.snake[square_num - 1].ycor()
            self.snake[square_num].goto(new_x, new_y)
        self.head.forward(10)

    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(0.5, 0.5, 0.5)
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.setheading(0)


