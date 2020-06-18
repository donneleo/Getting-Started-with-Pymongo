import tkinter as tk
from tkinter import *
import pymongo

client = pymongo.MongoClient("**************************")
db = client.test
mycol = db["names"]

def add_to_database():
    firstName = str(e1.get())
    surname = str(e2.get())
    mydict = { "First Name": firstName, "Surname": surname}
    x = mycol.insert_one(mydict)
    print("Name Added to Database")
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

app = Tk()
tk.Label(app, text="First Name").grid(row=0)
tk.Label(app, text="Last Name").grid(row=1)

e1 = tk.Entry(app)
e2 = tk.Entry(app)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(app, text='Enter', command=add_to_database).grid(row=3,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)

app.mainloop()
tk.mainloop()
