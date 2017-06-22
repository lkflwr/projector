"""      turtle-example-suite:

         tdemo_round_dance.py

(Needs version 1.1 of the turtle module that
comes with Python 3.1)

Dancing turtles have a compound shape
consisting of a series of triangles of
decreasing size.

Turtles march along a circle while rotating
pairwise in opposite direction, with one
exception. Does that breaking of symmetry
enhance the attractiveness of the example?

Press any key to stop the animation.

Technically: demonstrates use of compound
shapes, transformation of shapes as well as
cloning turtles. The animation is
controlled through update().
"""

from turtle import *

def stop():
    global running
    running = False

def main():
    global running
    clearscreen()   #
    bgcolor("white")
    #tracer(False)
    delay(10)
    triangle= ((0,0),(0.5*20,0.88*20),(-0.5*20,0.88*20))
    register_shape("tst",triangle)
    shape("tst")
    f =   0.793402
    phi = 9.064678
    s = 5
    c = 1

    # create triangle
    shapesize(10)
    pu()
    setpos(0, 0)

    # Rotate
    running = True
    onkeypress(stop)
    listen()
    while running:
        ta = -1
        tilt(ta)
        update()
    return "DONE!"

if __name__=='__main__':
    print(main())
    mainloop()

