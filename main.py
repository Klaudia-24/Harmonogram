from tkinter import *

def create_gui():
    root = Tk()
    root.title("Activities schedule")
    root.geometry('1000x500')
    root.resizable(0, 0)

    mainFrame = Frame(root)
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=3)

    controlFrame = Frame(mainFrame, bg='#668cff', highlightthickness=3, width=200, height=500)
    controlFrame.grid(row=0, column=0, sticky=W)

    displayFrame = Frame(mainFrame, bg='#cce0ff', highlightthickness=3, width=800, height=500)
    displayFrame.columnconfigure(0, weight=1)
    displayFrame.columnconfigure(1, weight=3)
    displayFrame.columnconfigure(2, weight=1)
    displayFrame.grid(row=0, column=1, sticky=E)

    label_2 = Label(displayFrame, text="05 July 2021", bg="#1a75ff", fg="white", padx=10, pady=10, font=(14))
    label_2.grid(row=0, column=1)
    prevButton = Button(displayFrame, text="<", bg='#002699', fg="white", font=(28))
    prevButton.grid(row=1, column=0, sticky=W)
    nextButton = Button(displayFrame, text=">", bg='#002699', fg="white", font=(58))
    nextButton.grid(row=1, column=2, sticky=E)

    calendarFrame = Frame(displayFrame, bg='#99c2ff', highlightthickness=3, width=750, height=450)
    calendarFrame.grid(row=1, column=1, sticky=E)

    mainFrame.pack(fill="both", expand="true")
    root.mainloop()

def __main__():
    create_gui()

if __name__ == '__main__':
    __main__()

