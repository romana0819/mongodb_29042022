# Demo MongoDB
import pymongo

# Connect 
connectstring = "mongodb+srv://romanamac:<password>@cluster0.2kbxf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(connectstring)

# Create
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Create a new document 
#mycol.insert_one({"-id":101, "companyname":"Kea", "contact":"Tue Hellstern"})
#mycol.insert_one({"-id":102, "companyname":"CPH Business", "contact":"Ole Hansen"})
#mycol.insert_one({"-id":103, "companyname":"ITU", "contact":"Peter Jensen"})
#mycol.insert_one({"-id":104, "companyname":"Something", "contact":"Ole Rasmusen", "country":"UK"})

#Find/Show/print 
#Find all
#for x in mycol.find():
#   print(x)

# Select columns

# Exclude id and lastname
#for x in mycol.find({},{ " _id": 0, "companyname": 0}):
#   print(x)

#Drop/Delete collection
#mycol.drop()

myquery = { "companyname": "Kea" }
newvalues = { "$set": { "companyname": "New Kea" } }
mycol.update_one(myquery, newvalues)






