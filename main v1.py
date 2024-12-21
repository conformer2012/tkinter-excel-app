import tkinter as tk
from tkinter import ttk
import openpyxl

root = tk.Tk()
root.geometry('500x500')
root.title("Tkinter Training")

style = ttk.Style(root)
# root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-light")

frame = ttk.Frame(root)
frame.pack()

frmWidget = ttk.LabelFrame(frame, text="Insert Row")
frmWidget.grid(row=0, column=0)

lblName = tk.Label(frmWidget, text="User Name")
lblName.grid(row=1, column=0)
txtName = ttk.Entry(frmWidget)
txtName.insert(0, "Name")
txtName.bind('<FocusIn>', lambda e: txtName.delete('0', 'end'))
txtName.grid(row=1, column=1)

lblAge = tk.Label(frmWidget, text="Age")
lblAge.grid(row=2, column=0, sticky='ew')
spinAge = ttk.Spinbox(frmWidget, from_=5, to=50)
spinAge.grid(row=2, column=1, sticky='ew')


root.mainloop()
