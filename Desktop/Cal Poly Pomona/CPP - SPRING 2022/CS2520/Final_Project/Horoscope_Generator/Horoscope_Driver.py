import Horoscope_OOP as H
from tkinter import *
from tkinter import Button

from PIL import ImageTk, Image


# Define entry_clear function in the box
def entry_clear(e):
    if month_entry.get() == 'ex: 11 or Nov' or date_entry.get() == 'ex: 1 - 31':
        month_entry.delete(0, END)
        date_entry.delete(0, END)


def destroy_display():
    root.destroy()


# display zodiac sign with the image
def display_zodiac(sign, image):
    root.destroy()

    # get_zodiac(month_entry, date_entry)

    # define image create image after the first destroyed
    sign_generated = Tk()
    sign_generated.title("SHOW ZODIAC")
    sign_generated.geometry('625x350')  # adjust size of the window
    sign_generated.resizable(width=False, height=False)  # prevent to resize the app

    # create a new canvas
    new_canvas = Canvas(sign_generated, width=625, height=350, bd=0, highlightthickness=0)
    new_canvas.pack(fill="both", expand=True)

    # define image
    new_image = ImageTk.PhotoImage(Image.open(image))

    # set image in Canvas
    new_canvas.create_image(0, 0, image=new_image, anchor="nw")

    new_canvas.create_text(425, 50, text="Your Sign is " + sign, font=("Helvetica", 18), fill="white")
    sign_generated.mainloop()

    # define image
    new_bg = ImageTk.PhotoImage(file=image)

    # set image in Canvas
    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")

    # Add label
    my_canvas.create_text(425, 50, text="Your Sign is " + sign, font=("Helvetica", 18), fill="white")


def input_validation(month_input, date_input):
    try:
        month = int(month_entry)
        date = int(date_entry)
        if month > 12 and date > 31:
            # display that the date and month might be out of range
            my_canvas.create_text(425, 50, text="date or month might be out of range", font=("Helvetica", 18), fill="white")
        else:
            return get_zodiac(month, date)
    except TypeError:
        my_canvas.create_text(425, 50, text="Invalid Input!! \nPlease follow the format!!", font=("Helvetica", 18),
                              fill="white")

def get_zodiac(month, date):
    # need to add try ad exception
    # Finding the horoscope sign (return tuple)??
    if (month == 3 and date >= 21) or (month == 4 and date < 20):
        return "ARIES"

    elif (month == 4 and date >= 20) or (month == 5 and date < 21):
        return "TAURUS"

    elif (month == 5 and date >= 21) or (month == 6 and date < 21):
        return "GEMINI"

    elif (month == 6 and date >= 21) or (month == 7 and date < 23):
        return "CANCER"

    elif (month == 7 and date >= 23) or (month == 8 and date < 23):
        return "LEO"

    elif (month == 8 and date >= 23) or (month == 9 and date < 23):
        return "VIRGO"

    elif (month == 9 and date >= 23) or (month == 10 and date < 23):
        return "lIBRA"

    elif (month == 10 and date >= 23) or (month == 11 and date < 22):
        return "SCORPIO"

    elif (month == 11 and date >= 22) or (month == 12 and date < 22):
        return "SAGITTARIUS"

    elif (month == 12 and date >= 22) or (month == 1 and date < 20):
        return "CAPRICORN"

    elif (month == 1 and date >= 20) or (month == 2 and date < 19):
        return "AQUARIUS"

    elif (month == 2 and date >= 19) or (month == 3 and date < 21):
        return "PISCES"


# =====================================================================================================
# END OF METHODS
# =====================================================================================================


# =====================================================================================================
# MAIN
# =====================================================================================================
# define the root
zodiac = H.Horoscope()

root = Tk()
root.title("HOROSCOPE GENERATOR")
root.geometry('625x350')  # adjust size of the window
root.resizable(width=False, height=False)  # prevent to resize the app

# create a canvas
my_canvas = Canvas(root, width=625, height=350, bd=0, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# define image
bg = ImageTk.PhotoImage(file="background_horoscope.gif")

# set image in Canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# Add label
my_canvas.create_text(425, 50, text="Check Your Sign Here...", font=("Helvetica", 18), fill="white")
my_canvas.create_text(380, 140, text="Month", font=("Helvetica", 16), fill="white")
my_canvas.create_text(380, 190, text="Date", font=("Helvetica", 16), fill="white")

# define input box and create an entry widget
month_entry = Entry(root, font=("Helvetica", 12), width=10, bg="white", borderwidth=5)
date_entry = Entry(root, font=("Helvetica", 12), width=10, bg="white", borderwidth=5)
month_entry.insert(0, "ex: 1 for Jan")
date_entry.insert(0, "ex: 1 - 31")

# Bind the Entry boxes
month_entry.bind("<Button-1>", entry_clear)
date_entry.bind("<Button-1>", entry_clear)

# add the entry boxes to the canvas
month_window = my_canvas.create_window(425, 125, anchor="nw", window=month_entry)
date_window = my_canvas.create_window(425, 175, anchor="nw", window=date_entry)

sign = input_validation(month_entry, date_entry)

# add entry button
continue_button = Button(root, text="Continue", font=("Helvetica", 14), width=12,
                         command=lambda: display_zodiac(sign, "Background Image.png"))
continue_button_window = my_canvas.create_window(370, 250, anchor="nw", window=continue_button)

root.mainloop()
