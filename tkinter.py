import tkinter as tk
from tkinter import ttk
win=tk.TK()
win.title("TAB Control")
nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='ONE')
nb.add(page2,text='TWO')