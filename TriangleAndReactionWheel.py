from turtle import *
import csv

def stop():
    global running
    running = False

def main():
    global running
    clearscreen()   #
    with open('TheMovie.csv', newline='') as csvfile:
        movie = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        row = next(movie)
        T = row[0]
        bgcolor("white")
        row =next(movie)
        # create triangle
        partdef = row[0]
        part =eval(partdef)
        register_shape("tst",part)
        shape("tst")
        row = next(movie)
        setpos(row[0],row[1])
        # Rotate
        running = True
        onkeypress(stop)
        listen()

        frame = next(movie)
        tilt(-frame[0])
        delay(T*1000)
        while running:
            frame = next(movie)
            tilt(-frame[0]*T)
            update()
        return "DONE!"

if __name__=='__main__':
    print(main())
    mainloop()

