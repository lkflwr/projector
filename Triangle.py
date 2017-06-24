from turtle import *
import csv

def stop():
    global running
    running = False

def main():
    global running
    clearscreen()   #
    bgcolor("white")

    # create triangle
    triangle= ((0,0),(-0.88*250,0.5*250),(-0.88*250,-0.5*250))
    register_shape("tst",triangle)
    shape("tst")

    setpos(0, 0)
    # Rotate
    running = True
    onkeypress(stop)
    listen()
    with open('alfa_dot.csv', newline='') as csvfile:
        film = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
        T_list=next(film)
        T=T_list[0]
        alfa_dot = next(film)
        tilt(-alfa_dot[0])
        delay(T*1000)
        while running:
            alfa_dot = next(film)
            tilt(-alfa_dot[0]*T)
            update()
        return "DONE!"

if __name__=='__main__':
    print(main())
    mainloop()

