import turtle
from turtle import *

tracer(0)

count_triangle = 0.3  # (0.3:1)
speed_fg = 0.5  # (0 ; 1)
width = 300
height = 300
mash = width * 0.1

setup(width, height)

hideturtle()
pensize(2)
title("💀это навечно💀")


def triangle(a):  # исунок одного треугольника
    fd(a)
    right(120)
    fd(a)
    right(120)
    fd(a)
    right(120)


def wr_tr(a):  # рисунок самого фрактала как 1 кадр и размер одной стороны наибольшего треугольника равна a
    if a <= mash * count_triangle:
        return
    triangle(a)
    wr_tr(a / 2)
    fd(a)
    triangle(a)
    wr_tr(a / 2)
    fd(a)
    rt(120)
    fd(a * 2)
    rt(120)
    triangle(a)
    wr_tr(a / 2)
    fd(a * 2)
    rt(120)


up()
setpos(-(width / 2 - width * 0.1), height / 2 - height * 0.1)  # перенос черепахи в левый угол
down()


def g(a):  # рекурсия для вызова фрактала как анимация
    clear()
    if a >= mash * 2:
        update()
        return
    wr_tr(a * 10)
    update()
    g(a + speed_fg)


while True:  # постоянный вызов с бесконечным приближением
    g(mash)
done()
