import random
import sys
import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                "Washinton,DC", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", 
                "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
                "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", 
                "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
                "Wyoming"]

rand_state = random.choice(state_list)
my_text = ("The State you should visit is", rand_state)

def popup_bonus():
    win = tk.Toplevel()
    win.wm_title("Random State Generator")

    l = tk.Label(win, text=my_text )
    l.grid(row=10, column=15)


def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)

class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.button_bonus = ttk.Button(self, text="Vacation? Where to?", command=popup_bonus)
        self.button_bonus.pack()

        self.button_bonus = ttk.Button(self, text="Restart", command=restart_program)
        self.button_bonus.pack()
root = tk.Tk()

app = Application(root)

root.mainloop()
