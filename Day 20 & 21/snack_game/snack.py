from turtle import Turtle


class Snack:
    def __init__(self):
        self.Blocks = []
        self.create_snack()

        self.head = self.Blocks[0]
        self.last_seg = self.Blocks[2]

    def create_snack(self):
        count = 0
        for _ in range(3):
            count += 20
            new_block = Turtle(shape="square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(x=0 - count, y=0)
            self.Blocks.append(new_block)

    def up(self):
        if self.head.heading() not in (270.0, 90.0):
            self.head.setheading(90)

    def down(self):
        if self.head.heading() not in (270.0, 90.0):
            self.head.setheading(270)

    def left(self):
        if self.head.heading() not in (180.0, 0.0):
            self.head.setheading(180)

    def right(self):
        if self.head.heading() not in (180.0, 0.0):
            self.head.setheading(0)

    def move(self):
        for i in range(len(self.Blocks) - 1, 0, -1):
            self.Blocks[i].goto(self.Blocks[i - 1].xcor(), self.Blocks[i - 1].ycor())
        self.head.fd(20)

    def get_longer(self):
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto(self.last_seg.pos())
        self.Blocks.append(new)
        self.last_seg = new

    def check_wall(self):

        if self.Blocks[1].xcor() > 290:
            return True
        elif self.Blocks[1].xcor() < -290:
            return True
        elif self.Blocks[1].ycor() > 290:
            return True
        elif self.Blocks[1].ycor() < -290:
            return True

    def ret_snack_head_loc(self):
        return self.head.xcor(), self.head.ycor()
