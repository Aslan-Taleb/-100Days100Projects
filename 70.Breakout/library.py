from turtle import Screen
from player import *
from blocks import *
from ball import *
from score import *
import pygame

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=1400, height=760)
screen.title("Breakout by AslaN")
screen.tracer(0)
screen.listen()

player = Player()
blocks = Blocks()
ball = Ball()
score = Score_lives(-600)
lives = Score_lives(600)
blocks.add_blocks()


screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")


def move_player_to_click(x, y):
    player.move_to(x)


screen.onclick(move_player_to_click)


def game_reset():
    ball.ball_reset()
    score.reset_score()
    blocks.reset_blocks()
    player.reset_player()


def sounds():
    pygame.mixer.init()
    bip_sound = pygame.mixer.Sound("sounds/Blip.wav")
    bip_sound.play()


def background():
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/background.mp3')
    pygame.mixer.music.play(-1)


screen.onkey(game_reset, "space")
