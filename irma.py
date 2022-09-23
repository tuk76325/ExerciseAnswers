import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    file = open("data/irma.csv", "r")
    lines = file.readlines()
    for row in lines[1:]:
        vals = row.strip().split(',')
        t.goto(float(vals[3]), float(vals[2]))
        if float(vals[4]) < 70:
            t.color('white')
            t.pensize(1)
        elif 70 <= float(vals[4]) <= 96:
            t.color('blue')
            t.pensize(3)
            t.write('1')
        elif 96 < float(vals[4]) <= 110:
            t.color('green')
            t.pensize(5)
            t.write('2')
        elif 110 < float(vals[4]) <= 130:
            t.color('yellow')
            t.pensize(7)
            t.write('3')
        elif 130 < float(vals[4]) <= 155:
            t.color('orange')
            t.pensize(9)
            t.write('4')
        elif 155 < float(vals[4]):
            t.color('red')
            t.pensize(11)
            t.write('5')
    turtle.exitonclick()

if __name__ == "__main__":
    irma()
