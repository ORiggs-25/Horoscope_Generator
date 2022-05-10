from tkinter import *
from tkinter import PhotoImage
from tkvideo import *
from PIL import ImageTk, Image

root = Tk()
root.title("HOROSCOPE GENERATOR")
root.geometry('650x550')        # adjust size of the window


# add image file
bg = ImageTk.PhotoImage(file="background_horoscope.gif")


result = Label(root, image=bg)


# show image using label
result.place(x=0, y=0)

result.grid(row=4, column=0, columnspan=2)

# prompt the user to enter date and month
def get_zodiac(date, month):
    global result
    result.grid_forget()

    bg = ImageTk.PhotoImage(file="background_horoscope.gif")

    # need to add try ad exception
    date = int(entry1.get())
    month = int(entry2.get())

    # Finding the horoscope sign
    if (month == 3 and date >= 21) or (month == 4 and date < 20):
        result = Label(root, text="YOUR ZODIAC SIGN IS ARIES", borderwidth=14, bg="white")
        result.config(font=("Britannic Bold", 18))
        result = Label(root, image=bg)
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 4 and date >= 20) or (month == 5 and date < 21):
        result = Label(root, text="YOUR ZODIAC SIGN IS TAURUS", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 5 and date >= 21) or (month == 6 and date < 21):
        result = Label(root, text="YOUR ZODIAC SIGN IS GEMINI", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 6 and date >= 21) or (month == 7 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS CANCER", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 7 and date >= 23) or (month == 8 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS LEO", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 8 and date >= 23) or (month == 9 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS VIRGO", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 9 and date >= 23) or (month == 10 and date < 23):
        result = Label(root, text="YOUR ZODIAC SIGN IS LIBRA", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 10 and date >= 23) or (month == 11 and date < 22):
        result = Label(root, text="YOUR ZODIAC SIGN IS SCORPIO", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 11 and date >= 22) or (month == 12 and date < 22):
        result = Label(root, text="YOUR ZODIAC SIGN IS SAGITTARIUS", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 12 and date >= 22) or (month == 1 and date < 20):
        result = Label(root, text="YOUR ZODIAC SIGN IS CAPRICORN", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 1 and date >= 20) or (month == 2 and date < 19):
        result = Label(root, text="YOUR ZODIAC SIGN IS AQUARIUS", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    elif (month == 2 and date >= 19) or (month == 3 and date < 21):
        result = Label(root, text="YOUR ZODIAC SIGN IS PISCES", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)

    else:
        result = Label(root, text="YOUR INPUTS ARE FALSE", borderwidth=12, bg="white")
        result.config(font=("Britannic Bold", 18))
        result.grid(row=4, column=0, columnspan=2)


label1 = Label(root, text="FIND YOUR HOROSCOPE HERE", borderwidth=10, fg="blue")
label1.config(font=("Britannic Bold", 18))
label1.grid(row=0, column=0, columnspan=3)

label2 = Label(root, text="BIRTH DATE :", borderwidth=2, fg="black")
label2.config(font=("Britannic Bold", 15))
label2.grid(row=1, column=0)

label3 = Label(root, text="BIRTH MONTH :", borderwidth=2, fg="black")
label3.config(font=("Britannic Bold", 15))
label3.grid(row=2, column=0)

entry1 = Entry(root, borderwidth=3, width=7)
entry1.grid(row=1, column=0)

entry2 = Entry(root, borderwidth=3, width=7)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)

date = entry1.get()
month = entry2.get()
get_button = Button(root, text="GET ZODIAC SIGN", anchor=CENTER, command=lambda: get_zodiac(date, month), height=2,
                    width=20, bg="purple", fg="white")

get_button.grid(row=3, column=0, columnspan=2)
root.mainloop()

