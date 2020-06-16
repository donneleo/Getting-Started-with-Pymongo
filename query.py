import pymongo

client = pymongo.MongoClient("mongodb+srv://donneleo:******@practicedatabase-lqlvk.mongodb.net/*******?retryWrites=true&w=majority")
db = client.test

mycol = db["names"]
query = { "First Name": "Eoin"}

mydoc = mycol.find(query)
for x in mydoc:
    print(x)
