from library import *


def victory():
    screen.clear()
    screen.bgcolor("black")
    screen.title("DEFEAT")
    pen = Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("VICTORY", align="center", font=("Courier", 50, "normal"))
    button_play_again()


def game_over():
    screen.clear()
    screen.bgcolor("black")
    screen.title("DEFEAT")
    pen = Turtle()
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write("DEFEAT", align="center", font=("Courier", 50, "normal"))
    button_play_again()


def button_play_again():
    # Create the Play Again button
    play_again_button = Turtle()
    play_again_button.color("white")
    play_again_button.penup()
    # play_again_button.hideturtle()
    play_again_button.goto(0, -50)
    play_again_button.write("Play Again", align="center",
                            font=("Courier", 20, "normal"))


def main():
    background()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.mySpeed)
        ball.move_ball()
        for block in blocks.list_blocks:
            if ball.distance(block) < 30:
                ball.bounce_ball_contact()
                block.clear()
                block.hideturtle()
                blocks.list_blocks.remove(block)
                score.increase_score()
                sounds()
                break
        if (ball.distance(player) < 30):
            ball.bounce_ball_contact()
            ball.increase_speed()
            sounds()
        if ball.y_pos < -400:
            game_reset()
            lives.decrease_lives()
            ball.reset_speed()
        if ball.y_pos > 500:
            ball.my_direction_y = -(ball.my_direction_y)
            ball.ball_reset()
        if len(blocks.list_blocks) == 0:
            game_is_on = False
            victory()
        if lives.lives == 0:
            game_over()
            game_is_on = False
    screen.mainloop()


screen.onkey(game_reset, "space")


main()
