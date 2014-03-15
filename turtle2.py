#!/usr/bin/python
"""       turtle-example-suite:

              tdemo_peace.py

A very simple drawing suitable as a beginner's
programming example.

Uses only commands, which are also available in
old turtle.py.

Intentionally no variables are used except for the
colorloop:
"""

from turtle import *

def main():
    raw_input()
    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")

    reset()
    s = Screen()
    up()
    goto(-320,-195)
    width(70)

    for pcolor in peacecolors:
        color(pcolor)
        down()
        forward(640)
        up()
        backward(640)
        left(90)
        forward(66)
        right(90)
        raw_input()

    width(25)
    color("white")
    goto(0,-170)
    down()
    raw_input()

    circle(170)
    raw_input()
    left(90)
    forward(340)
    up()
    raw_input()
    left(180)
    forward(170)
    right(45)
    raw_input()
    down()
    forward(170)
    raw_input()
    up()
    backward(170)
    raw_input()
    left(90)
    down()
    raw_input()
    forward(170)
    up()
    raw_input()

    goto(0,300) # vanish if hideturtle() is not available ;-)
    return "Done!!"

if __name__ == "__main__":
    main()
    mainloop()