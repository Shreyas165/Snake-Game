import turtle
import time
import random

class SnakeGame:
    def __init__(self):
        self.delay = 0.1
        self.wn = turtle.Screen()
        self.head = None
        self.food = None
        self.segments = []
        self.score = 0

        self.setup_screen()
        self.initialize_head()
        self.initialize_food()
        self.score_display = None
        self.score_display = self.setup_score_display()
        self.handle_input()
        self.game_loop()
    def setup_screen(self):
        self.wn.title("Snake Game")
        self.wn.bgcolor("black")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)

    def initialize_head(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "Right"

    def initialize_food(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

    def setup_score_display(self):
        score_d = turtle.Turtle()
        score_d.speed(0)
        score_d.color("white")
        score_d.penup()
        score_d.hideturtle()
        score_d.goto(0, 260)
        score_d.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        return score_d

    def handle_input(self):
        def go_up():
            if self.head.direction != "down":
                self.head.direction = "up"

        def go_down():
            if self.head.direction != "up":
                self.head.direction = "down"

        def go_left():
            if self.head.direction != "right":
                self.head.direction = "left"

        def go_right():
            if self.head.direction != "left":
                self.head.direction = "right"

        self.wn.listen()
        self.wn.onkey(go_up, "Up")
        self.wn.onkey(go_down, "Down")
        self.wn.onkey(go_left, "Left")
        self.wn.onkey(go_right, "Right")

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def check_border_collision(self):
        if (
            self.head.xcor() > 290
            or self.head.xcor() < -290
            or self.head.ycor() > 290
            or self.head.ycor() < -290
        ):
            self.teleport_to_opposite_border()

    def teleport_to_opposite_border(self):
        x, y = self.head.xcor(), self.head.ycor()

        if self.head.xcor() > 290:
            self.head.goto(-290, y)
        elif self.head.xcor() < -290:
            self.head.goto(290, y)
        elif self.head.ycor() > 290:
            self.head.goto(x, -290)
        elif self.head.ycor() < -290:
            self.head.goto(x, 290)

    def check_food_collision(self):
        if self.head.distance(self.food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            self.food.goto(x, y)
            self.create_segment()
            self.score += 1
            self.update_score()

    def move_segments(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        if len(self.segments) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.segments[0].goto(x, y)

    def check_body_collision(self):
        for segment in self.segments:
            if self.head.distance(segment) < 20:
                self.reset_game()

    def reset_game(self):
        self.head.goto(0, 0)
        self.head.direction = "Right"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.score = 0
        self.update_score()

    def create_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        self.segments.append(new_segment)

    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_loop(self):
        while True:
            self.wn.update()
            self.check_border_collision()
            self.check_food_collision()
            self.move_segments()
            self.move()
            self.check_body_collision()
            time.sleep(self.delay)

# Main execution
if __name__ == "__main__":
    snake_game = SnakeGame()
