import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pymongo

def add_name():
    client = pymongo.MongoClient("************")
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

    def exit_window():
        app_add.destroy()

    app_add = Tk(className=" Add")
    app_add.geometry("200x125")
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
    tk.Button(app_add, text="Exit", command=exit_window).grid(row=4,column=1,sticky=tk.W,pady=4)

def search_name():
    client = pymongo.MongoClient("***************")
    db = client.test
    mycol = db["names"]

    def show_results(result):
        results = []
        number_elements = 0
        for x in result:
            results.append(x)
            number_elements +=1
            results.append("\n")
            results.append("\n")
        if(number_elements == 0):
            messagebox.showinfo(" Search Results", "No Match Found")
        else:
            messagebox.showinfo(" Search Results", results)

    def search_database():
        firstName = str(e3.get())
        query = { "First Name": firstName}
        mydoc = mycol.find(query)
        show_results(mydoc)
        e3.delete(0, tk.END)
        app_search.destroy()

    def exit_search_window():
        app_search.destroy()

    app_search = Tk(className=" Search")
    app_search.geometry("200x100")
    tk.Label(app_search, text="First Name").grid(row=0)
    e3 = tk.Entry(app_search)
    e3.grid(row=0, column=1)
    tk.Button(app_search, text='Search', command=search_database).grid(row=3,
                                                                       column=1,
                                                                       sticky=tk.W,
                                                                       pady=4)
    tk.Button(app_search, text="Exit", command=exit_search_window).grid(row=4,column=1,sticky=tk.W,pady=4)

def end_app():
    app.destroy()

app = Tk(className = " Cill Dara Hunting Search")
app.geometry("240x125")

button1 = tk.Button(app, text="Add to Database", command=add_name).grid(row=1, column=1, padx=8, pady=8)
button2 = tk.Button(app, text="Search the Databse", command=search_name).grid(row=1, column=2, padx=8, pady=8)
button3 = tk.Button(app, text="Close App", command=end_app).grid(row=3, column=2, pady=15)

app.mainloop()
tk.mainloop()
