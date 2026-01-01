from turtle import *
import time

colors = ["white", "red", "yellow", "blue","brown","purple"]#!!!!!!!!!!!! len(colors) >=3 !!!!!!!!!!!
width = 300
height = 1080
bg_color = "green"
len_lines = 15
speed_light = 3
rad_light = len_lines / 3
count_lines = 30
h = height / (count_lines + 1)

setup(width, height)
bgcolor(bg_color)
pensize(2)
tracer(0)
title("🎄Merry Christmas🎄")
hideturtle()

def write_line(a):
    if a >= len(colors) or a < -1:
        a = 0

    if pos()[0] >= width / 2:
        return

    pos1 = pos()
    left(45)
    fd(len_lines)
    pos2 = pos()
    up()
    goto(pos1)
    dot(rad_light, colors[a])
    goto(pos2)
    down()
    rt(90)
    pos1 = pos()
    fd(len_lines)
    pos2 = pos()
    up()
    goto(pos1)
    dot(rad_light, colors[a])
    goto(pos2)
    down()
    lt(45)
    write_line(a + 1)


def write_lines(a=1, c=0):
    if a > count_lines:
        return
    elif c == len(colors) - 1:
        c = 0
    up()
    goto(width / 2 - width, height / 2 - (h * a))
    down()
    write_line(c)
    write_lines(a + 1, c + 1)


while True:
    for i in range(len(colors)):
        write_lines(a=1, c=i)
        update()
        clear()
        time.sleep(1 / speed_light)
mainloop()
