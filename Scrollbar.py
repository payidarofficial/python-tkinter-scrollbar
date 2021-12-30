# Pâyidar
# Tkinter İle Basit Arayüz.

from tkinter import *
from tkinter import ttk
import tkinter

# Arayüz Kodlarımız

root = Tk();
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set)

for line in range(101):
    mylist.insert(END, str(line) + " Yazı.")

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)

root.mainloop()