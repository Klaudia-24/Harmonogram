from tkinter import *
import sys
from UI_main_window import *

def create_gui():
    root = Tk()
    root.title("Activities schedule")
    root.geometry('1000x500')
    #mainFrame = Frame(root, bg='#003d99')
    mainFrame = Frame(root, bg='#79d279')
    mainFrame.pack(fill="both", expand="true")

    mainFrame.columnconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=3)

    controlFrame = Frame(mainFrame, bg='#668cff', highlightbackground="red", highlightthickness=3, width=200)
    #label_1 = Label(mainFrame, text="controlFrame", bg="red", fg="white", padx=10, pady=10)
    #label_1.pack()
    controlFrame.grid(row=0, column=0, ipadx=20, ipady=500)

    displayFrame = Frame(mainFrame, bg='#cce0ff', highlightbackground="blue", highlightthickness=3, width=800)
    #label_2 = Label(mainFrame, text="displayFrame", bg="blue", fg="white", padx=10, pady=10)
    #label_2.pack()
    # prevButton = Button(displayFrame, text="prev", bg='#002699', fg="white", font=(12))
    # prevButton.grid(row=3, column=1, sticky=W)
    # nextButton = Button(displayFrame, text="next", bg='#002699', fg="white", font=(12))
    # nextButton.grid(row=3, column=2, sticky=E)
    displayFrame.grid(row=0, column=1, ipadx=20, ipady=500)



    root.mainloop()

def create_gui_2():
    root = Tk()
    root.title("Activities schedule")
    root.geometry('1000x500')
    # mainFrame = Frame(root, bg='#003d99')
    mainFrame = Frame(root, bg='#79d279')
    mainFrame.pack(fill="both", expand="true")

    mainFrame.columnconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=3)

    controlFrame = Frame(mainFrame, bg='#668cff', highlightthickness=3, width=200, height=500)
    label_1 = Label(controlFrame, text="controlFrame", bg="red", fg="white", padx=10, pady=10)
    label_1.grid(row=0, column=0)
    controlFrame.grid(row=0, column=0)

    displayFrame = Frame(mainFrame, bg='#cce0ff', highlightthickness=3, width=800, height=500)
    displayFrame.columnconfigure(0, weight=1)
    displayFrame.columnconfigure(1, weight=3)
    displayFrame.columnconfigure(2, weight=1)

    label_2 = Label(displayFrame, text="displayFrame", bg="blue", fg="white", padx=10, pady=10)
    label_2.grid(row=0, column=1)
    prevButton = Button(displayFrame, text="<", bg='#002699', fg="white", font=(28))
    prevButton.grid(row=1, column=0, sticky=W)
    nextButton = Button(displayFrame, text=">", bg='#002699', fg="white", font=(58))
    nextButton.grid(row=1, column=3, sticky=E)

    displayFrame.grid(row=0, column=1)

    root.mainloop()

def create_gui_3():
    # root window
    root = Tk()
    root.geometry("240x100")
    root.title('Login')
    root.resizable(0, 0)

    # configure the grid
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    # username
    username_label = Label(root, text="Username:")
    username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

    username_entry = Entry(root)
    username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

    # password
    password_label = Label(root, text="Password:")
    password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

    password_entry = Entry(root, show="*")
    password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

    # login button
    login_button = Button(root, text="Login")
    login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)

    root.mainloop()

def create_gui_4():
    master = Tk()
    master.title("grid() method")
    master.geometry("350x275")

    button1 = Button(master, text="button1")
    button1.grid(row=1, column=0)

    button2 = Button(master, text="button2")
    button2.grid(row=2, column=2)

    button3 = Button(master, text="button3")
    button3.grid(row=3, column=3)

    button4 = Button(master, text="button4")
    button4.grid(row=4, column=4)

    button5 = Button(master, text="button5")
    button5.grid(row=5, column=5)

    master.mainloop()

def create_gui_5():
    master = Tk()

    frame1 = Frame(master, width=200, height=200, bg="red")
    frame2 = Frame(master, width=200, height=200, bg="green")
    frame3 = Frame(master, width=200, height=200, bg="blue")
    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    frame3.grid(row=3, column=1)

    master.mainloop()

def create_gui_6():
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
   # create_gui_6()
   app = QtWidgets.QApplication(sys.argv)
   Dialog = QtWidgets.QDialog()
   ui = Ui_Dialog()
   ui.setupUi(Dialog)
   Dialog.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
    __main__()

