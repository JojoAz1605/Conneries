from turtle import*
import time
from random import randint

hexa = '0123456789ABCDEF'

def selectColor():
    """Retourne une couleur en hexa aléatoire"""
    color = '#'
    for i in range(6):
        color += hexa[randint(0, len(hexa)-1)]
    return color
        

speed(10000000)
left(90)
color("red")
screen = Screen()
screen.setup(1000, 1000)

def segment(longueur):
    forward(longueur)

def avance(longueur):
    penup()
    segment(longueur)
    pendown()

def croix(longueur):
    color('red')
    segment(longueur/2)
    right(90)
    segment(longueur)
    left(90)
    segment(longueur/2)
    left(180)
    avance(longueur)
    right(90)
    segment(longueur/2)
    right(90)
    segment(longueur)
    left(90)
    segment(longueur/2)

def frac(longueur, n):
    if n == 0:
        segment(longueur)
    else:
        color(selectColor())
        segment(longueur/2)
        right(90)
        frac(longueur, n-1)
        left(90)
        frac(longueur/2, n-1)
        left(180)
        avance(longueur)
        right(90)
        frac(longueur/2, n-1)
        right(90)
        frac(longueur, n-1)
        left(90)
        frac(longueur/2, n-1)
frac(60, 10)
