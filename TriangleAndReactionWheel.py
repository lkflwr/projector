from turtle import *
import csv

def stop():
    global running
    running = False

def main():
    global running
    clearscreen()   #
    s = Shape("compound")
    with open('TheMovie.csv', newline='') as csvfile:
        movie = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        row = next(movie)
        T = row[0]
        bgcolor("white")
        row =next(movie)
        Allparts=[]

        # create triangle
        partdef = row[0]
        part =eval(partdef)
        #s.addcomponent(part,"blue")
        register_shape("tst",part)
        shape("tst")
        Allparts.append(clone())
        row = next(movie)
        #setpos(row[0],row[1])
        # Rotate triangle
        frame = next(movie)
        #tilt(-frame[0])

        # create and add rectangle
        row= next(movie)
        partdef = row[0]
        part = eval(partdef)
        #s.addcomponent(part, "red")
        register_shape("tst2",part)
        shape("tst2")
        Allparts.append(clone())
        row= next(movie)
        setpos(row[0],row[1])
        # Rotate rectangle
        frame = next(movie)
        tilt(-frame[0])
        #register_shape("tst3",s)
        #shape("tst3")
        running = True
        onkeypress(stop)
        listen()


        delay(T*1000)
        while running:
            frame = next(movie)
            Allparts[0].tilt(-frame[0]*T)
            Allparts[1].tilt(-frame[1]*T)
            update()
        return "DONE!"

if __name__=='__main__':
    print(main())
    mainloop()

