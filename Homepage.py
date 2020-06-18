import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pymongo

def add_name():
    client = pymongo.MongoClient(
        "*****************************")
    db = client.test
    mycol = db["names"]

    def name_added():
        messagebox.showinfo( "Success", "Name Added")

    def add_to_database():
        firstName = str(e1.get())
        print(firstName)
        surname = str(e2.get())
        mydict = {"First Name": firstName, "Surname": surname}
        x = mycol.insert_one(mydict)
        name_added()
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)

    app_add = Tk()
    tk.Label(app_add, text="First Name").grid(row=0)
    tk.Label(app_add, text="Last Name").grid(row=1)

    e1 = tk.Entry(app_add)
    e2 = tk.Entry(app_add)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(app_add, text='Enter', command=add_to_database).grid(row=3,
                                                               column=1,
                                                               sticky=tk.W,
                                                               pady=4)

def search_name():
    client = pymongo.MongoClient(
        "**********************************")
    db = client.test
    mycol = db["names"]

    def show_results(result):
        print(result)

    def search_database():
        firstName = str(e3.get())
        query = { "First Name": firstName}
        mydoc = mycol.find(query)
        for x in mydoc.find({}, {"_id":0}):
            print(x)
        e3.delete(0, tk.END)

    app_search = Tk()
    tk.Label(app_search, text="First Name").grid(row=0)
    e3 = tk.Entry(app_search)
    e3.grid(row=0, column=1)
    tk.Button(app_search, text='Search', command=search_database).grid(row=3,
                                                                       column=1,
                                                                       sticky=tk.W,
                                                                       pady=4)


app = Tk()
button1 = tk.Button(app, text="Add to Database", command=add_name).grid(row=1, column=0)
button2 = tk.Button(app, text="Search the Databse", command=search_name).grid(row=1, column=2)

app.mainloop()
tk.mainloop()
