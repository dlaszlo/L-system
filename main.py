from lsystem import LSystem
from screen import Screen
from turtle import Turtle

# turtle = Turtle(800, 800, 100, 700)
# screen = Screen(turtle, 800, 800)
#
# l_system = LSystem("F-G-G",
#                    [("F", "F-G+F+G-F"),
#                     ("G", "GG")],
#                    {"F": lambda: turtle.draw(5),
#                     "G": lambda: turtle.draw(5),
#                     "-": lambda: turtle.rotate(-120),
#                     "+": lambda: turtle.rotate(120)},
#                    7)
# l_system.draw()

turtle = Turtle(800, 800)
screen = Screen(turtle, 800, 800)

l_system = LSystem("X",
                   [("X", "F+[[X]-X]-F[-FX]+X"),
                    ("F", "FF")],
                   {"F": lambda: turtle.draw(1),
                    "X": lambda: turtle.rotate(90),
                    "-": lambda: turtle.rotate(-25),
                    "+": lambda: turtle.rotate(25),
                    "[": lambda: turtle.push(),
                    "]": lambda: turtle.pop()},
                   8)
l_system.draw()

while screen.check_quit():
    screen.update()
    screen.delay(100)
