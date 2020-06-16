import pymongo


client = pymongo.MongoClient("mongodb+srv://donneleo:********@practicedatabase-lqlvk.mongodb.net/********?retryWrites=true&w=majority")
db = client.test

mycol = db["names"]
mydict = { "First Name": "Davin", "Surname": "Jackson" }

x = mycol.insert_one(mydict)
print(x)
